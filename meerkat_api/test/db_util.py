#!/usr/bin/env python3
"""
Utility functions for setting up the DB for Meerkat API tests

"""
from datetime import datetime, timedelta
import uuid
import random

from meerkat_api.test.test_data import codes, locations, cases, alerts, links


from meerkat_abacus import model


def insert_cases(session, variable):
    """ Add a variable with cases from the cases.py file in test_data
    
    Args: 
       session: db session
       variable: name of the varible from cases.py we want
    """
    session.query(model.Data).delete()
    session.bulk_save_objects(getattr(cases, variable))
    session.commit()

def insert_links(session, variable):
    """ Add a variable with links from the links.py file in test_data
    
    Args: 
       session: db session
       variable: name of the varible from links.py we want
    """
    session.query(model.Links).delete()
    session.bulk_save_objects(getattr(links, variable))
    session.commit()

def insert_alerts(session, variable):
    """ Add a variable with alerts from the alerts.py file in test_data
    
    Args: 
       session: db session
       variable: name of the varible from alerts.py we want
    """
    session.query(model.Alerts).delete()
    session.bulk_save_objects(getattr(alerts, variable))
    session.commit()


def insert_codes(session):
    """ Add the codes from the codes.py file in test_data
    
    Args: 
       session: db session
    """
    session.query(model.AggregationVariables).delete()
    session.bulk_save_objects(codes.codes)
    session.commit()
def insert_locations(session):
    """ Add the locations from the locations.py file in test_data
    
    Args: 
       session: db session
    """
    session.query(model.Locations).delete()
    session.bulk_save_objects(locations.locations)
    session.commit()
    


def create_category(session, variables, category, names=None):
    """
    Make sure the aggregation_variables table has only the variables
    specified with the given cateogry

    Args: 
       session: the db session
       variables: list of variable ids we want to add
       category: a single or list of categories to add to the variables
       names: If give we use those names for the variables, otherwise we just use the ids
    """

    if not isinstance(category, list):
        category = [category]
    if not names:
        names = variables
    if len(variables) != len(names):
        raise IndexError("Varibles and names need to have the same length")
    session.query(model.AggregationVariables).delete()
    session.commit()
    for i, v in enumerate(variables):
        session.add(model.AggregationVariables(
            id=v,
            name=names[i],
            category=category
        ))
    session.commit()

def create_data(session, variables,
                locations=(1,2,3,4), dates="year",
                clinic_types="hospital", geolocations="0,0"):
    """
    Makes sure the data table has records with the variables in the variables list

    Args: 
       session: db session
       variables: list of variable dicts to give the records
       locations: either one location tuple(country, region, dsitrict, clinic) to give all the records or a list of Locations
       dates: either year(to create dates for this year) or a list of dates to create
       clinic_types: either one clinic_type or list of clinics_types
    """
    session.query(model.Data).delete()
    session.commit()
    N = len(variables)
    if not isinstance(locations, list):
        locations = [locations for i in range(N)]
    if not isinstance(clinic_types, list):
        clinic_types = [clinic_types for i in range(N)]
    if not isinstance(geolocations, list):
        geolocations = [geolocations for i in range(N)]
        
    if dates == "year":
        year = datetime(datetime.now().year, 1, 1)
        days = (datetime.now() - year).days
        dates = []
        for i in range(N):
            date = year + timedelta(days=random.randint(0, days))
            dates.append(date)

    if len(locations) != N or len(dates) != N or len(clinic_types) != N or len(geolocations) != N:
        raise IndexError("Variables, locations, clinic_types, geolocations and dates need to have the same length")
    
    for i in range(N):
        session.add(model.Data(
            uuid=uuid.uuid4(),
            country=locations[i][0],
            region=locations[i][1],
            district=locations[i][2],
            clinic=locations[i][3],
            clinic_type=clinic_types[i],
            date=dates[i],
            variables=variables[i],
            geolocation=geolocations[i]
        ))
    session.commit()