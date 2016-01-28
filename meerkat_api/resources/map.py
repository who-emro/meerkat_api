"""
Resources for creating maps
"""
from flask_restful import Resource
from geojson import Point, FeatureCollection, Feature
from sqlalchemy import  extract, func, Integer
from datetime import datetime

from meerkat_api.util import row_to_dict, rows_to_dicts, is_child
from meerkat_api import db, app
from meerkat_abacus import model
from meerkat_abacus.model import Data
from meerkat_abacus.util import get_locations
from meerkat_api.authentication import require_api_key

class Clinics(Resource):
    """
    geojson for all clinics that are sublocation of location
    """
    def get(self, location_id):
        locations = get_locations(db.session)
        points = []
        for l in locations:
            if (locations[l].case_report and is_child(
                    location_id, l, locations) and locations[l].geolocation):
                lat, lng = locations[l].geolocation.split(",")

                p = Point((float(lng), float(lat)))
                points.append(Feature(geometry=p,
                                      properties={"name":
                                                  locations[l].name}))
        return FeatureCollection(points)

class MapVariable(Resource):
    """
    json object with a map of variable id
    """
    decorators = [require_api_key]
    def get(self, variable_id, interval="year"):
        vi= str(variable_id)
        year = datetime.now().year
        if interval == "year":
            results = db.session.query(
                func.sum(
                    Data.variables[vi].astext.cast(Integer)).label('value'),
                Data.geolocation,
                Data.clinic
        ).filter(Data.variables.has_key(vi),
                 extract('year', Data.date) == year).group_by("clinic",
                                                              "geolocation")
        locations = get_locations(db.session)
        ret = []
        for r in results.all():
            if r[1]:
                ret.append({"value": r[0], "geolocation": r[1].split(","),
                            "clinic": locations[r[2]].name})
        return ret
