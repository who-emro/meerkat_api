"""
Data resource for completeness data
"""
from flask_restful import Resource
from flask import jsonify
from sqlalchemy import extract, func, Integer, or_
from datetime import datetime, timedelta
import pandas as pd

from meerkat_api import db, app
from meerkat_api.resources.epi_week import EpiWeek, epi_week_start
from meerkat_abacus.model import Data, Locations
from meerkat_api.util import get_children
from meerkat_abacus.util import get_locations, epi_week_start_date
from meerkat_api.authentication import require_api_key
from meerkat_abacus.util import get_locations
from pandas.tseries.offsets import CustomBusinessDay

def series_to_json_dict(series):
    """
    Takes pandas series and turns into a dict with string keys

    Args: 
        series: pandas series
    
    Returns: 
       dict: dict
    """
    if series is not None:
        return dict( (str(key), value) for key, value in series.to_dict().items())
    else:
        return {}

class Completeness(Resource):
    """
    Return completeness data of variable. We calculate both a score based on the average of the last two epi weeks 
    and a timeline of the average number of records per week. We only allow one record per day. 

    We include data for both the given location and the sublocations. 

    Args: \n
        variable: variable_id\n
        location: location id
        number_per_week: expected number per week\n
        weekend: specified weekend days in a comma separated string 0=Mon
    Returns:\n
        completness data: {score: score, timeline: timeline, clinic_score: clinic:score, dates_not_reported: dated_not_reported}\n
    """
    decorators = [require_api_key]
    def get(self, variable, location, number_per_week, weekend=None):
        today = datetime.now()
        epi_year_weekday = epi_week_start_date(today.year).weekday()
        freq = ["W-MON", "W-TUE", "W-WED",
                "W-THU", "W-FRI", "W-SAT", "W-SUN"][epi_year_weekday]

        number_per_week = int(number_per_week)
        locs = get_locations(db.session)
        location = int(location)
        location_type = locs[location].level
        sublevels = {"country": "region",
                    "region": "district",
                    "district": "clinic",
                    "clinic": None}
        sublevel = sublevels[location_type]

        # get the data
        data = pd.read_sql(
            db.session.query(Data.region,
                             Data.district,
                             Data.clinic,
                             Data.date,
                             Data.variables[variable].label(variable)
            ).filter(Data.variables.has_key(variable),
                     or_(loc == location for loc in (Data.country,
                                                     Data.region,
                                                     Data.district,
                                                     Data.clinic))).statement,
            db.session.bind)

        if len(data) == 0:
            return {}

        # If today is the start of an epi week we do not want to include the current epi week
        if today.weekday() == epi_year_weekday:
            end_d = today - timedelta(days=1)
        else:
            end_d = today
            
        begining = epi_week_start_date(today.year)
        # We drop duplicates so each clinic can only have one record per day
        data = data.drop_duplicates(subset=["region", "district", "clinic", "date", variable])

        if sublevel:
            # We first create an index with sublevel, clinic, dates
            # Where dates are the dates after the clinic started reporting
            sublocations = []
            for l in locs.values():
                if l.parent_location == location and l.level == sublevel:
                    sublocations.append(l.id)
            tuples = []
            for name in sublocations:
                for clinic in get_children(name, locs):
                    start_date = locs[clinic].start_date
                    if start_date < begining:
                        start_date = begining
                    for d in pd.date_range(start_date, end_d, freq=freq):
                        tuples.append((name, clinic, d))

            new_index = pd.MultiIndex.from_tuples(tuples,
                                                  names=[sublevel, "clinic", "date"])

            completeness = data.groupby(
                [sublevel ,
                 "clinic",
                 pd.TimeGrouper(key="date", freq=freq, label="left")]
            ).sum().reindex(new_index)[variable].fillna(0).sort_index()

            # We only want to count a maximum of number per week per week
            completeness[completeness > number_per_week] = number_per_week
            
            location_completeness_per_week = completeness.groupby(level=2).mean()
            sublocations_completeness_per_week = completeness.groupby(level=[0,2]).mean()

            # Find last two weeks 
            idx = pd.IndexSlice
            last_two_weeks = location_completeness_per_week.index[-2:]

            # Get sublocation completeness for last two weeks as a percentage
            completeness_last_two_weeks = sublocations_completeness_per_week.loc[idx[:, last_two_weeks]]
            score = completeness_last_two_weeks.groupby(level=0).mean() / number_per_week * 100
            
            # Add current location 
            score[location] = location_completeness_per_week[last_two_weeks].mean() / number_per_week * 100

            # Sort the timeline data 
            timeline = {}
            for sl in sublocations_completeness_per_week.index.get_level_values(sublevel):
                sl_time = sublocations_completeness_per_week.iloc[
                sublocations_completeness_per_week.index.get_level_values(sublevel) == sl]
                timeline[str(sl)] = {
                    "weeks": sl_time.index.get_level_values("date"),
                    "values": sl_time}
            # Add current location 
            timeline[str(location)] = {
                "weeks": location_completeness_per_week.index,
                "values": location_completeness_per_week
            }
            # Calculate completness score for each clinic
            clinic_completeness_last_two_weeks = completeness.loc[idx[:,:,last_two_weeks]]
            clinic_scores = clinic_completeness_last_two_weeks.groupby(level=1).mean() / number_per_week * 100
            dates_not_reported = [] # Not needed for this level
            
        else:
            # Take into account clinic start_date 
            if locs[location].start_date > begining:
                begining = locs[location].start_date
            dates = pd.date_range(begining, end_d, freq=freq)
            completeness = data.groupby(
                pd.TimeGrouper(key="date", freq=freq, label="left")
            ).sum().fillna(0)[variable].reindex(dates).sort_index().fillna(0)
            
            timeline = {str(location): {
                "weeks": completeness.index.to_pydatetime(),
                "values": completeness.values}
            }
            last_two_weeks = completeness.index[-2:]
            score = pd.Series() 
            score.loc[location] = completeness[last_two_weeks].mean() / number_per_week * 100

            # Sort out the dates on which nothing was reported
            # Can specify on which weekdays we expect a record
            
            if not weekend:
                weekday_mask = "Mon Tue Wed Thu Fri"
            else:
                weekend = weekend.split(",")
                weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                weekday_mask = ""
                for i, w in enumerate(weekdays):
                    if i not in weekend and str(i) not in weekend:
                        weekday_mask = weekday_mask + weekdays[i] + " "
            
            bdays = CustomBusinessDay(weekmask=weekday_mask)
            expected_days = pd.date_range(begining, end_d, freq=bdays)

            found_dates = data["date"]
            dates_not_reported = expected_days.drop(
                found_dates.values,
                errors="ignore"
            ).to_pydatetime()
            clinic_scores = None # Not needed for this level

        return jsonify({"score": series_to_json_dict(score),
                        "timeline": timeline,
                        "clinic_score": series_to_json_dict(clinic_scores),
                        "dates_not_reported": dates_not_reported})

class NonReporting(Resource):
    """
    Returns all non-reporting clinics for the last num_weeks complete epi weeks .

    Args: \n
        variable: variable_id\n
        location: location\n
        num_weeks: number_of_weeks \n
   

    Returns:\n
        list_of_clinics
    """
    decorators = [require_api_key]
    def get(self, variable, location, num_weeks=2):
        locations = get_locations(db.session)
        location = int(location)
        clinics = get_children(location, locations)
        ew = EpiWeek()
        epi_week = ew.get()
        start_date = epi_week_start(epi_week["year"],
                                    epi_week["epi_week"]) - timedelta(days=7 * num_weeks)
        clinics_with_variable = [ r[0] for r in db.session.query(Data.clinic).filter(
            Data.variables.has_key(variable), Data.date > start_date).all()]
        non_reporting_clinics = []
        for clinic in clinics:
            if clinic not in clinics_with_variable:
                non_reporting_clinics.append(clinic)

        return {"clinics": non_reporting_clinics}


