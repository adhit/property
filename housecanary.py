import requests
from requests.auth import HTTPBasicAuth
import credentials # consists of two string vars: key and secret
from enum import Enum
from typing import List

class Levels(Enum):
    STATE = 'state'
    MSA = 'msa'
    METRODIV = 'metrodiv'
    ZIP = 'zip'

    @staticmethod
    def get_id_key(level):
        return {
            Levels.STATE: 'state',
            Levels.MSA: 'msa',
            Levels.METRODIV: 'metrodiv',
            Levels.ZIP: 'zip'
        }[level]

class Endpoints(Enum):
    HCRI = 'hcri' # HouseCanary Rental Index
    HPI_TS_FORECAST = 'hpi_ts_forecast' # House Price Index Forecast

class QueryMaker:
    '''The object that is making queries to HouseCanary API'''

    BASE_URL = 'https://api.housecanary.com/v2'
    TEST_KEY = 'test_NWLACMGVTYLH5M3I9LHA'
    TEST_SECRET = '11jJqQdUNRLtuQV5VtPqAT0yUY7Z4QhZ'

    def __init__(self):
        self.key = credentials.key
        self.secret = credentials.secret

    # returns a json string
    def query(self, level, id, endpoints: List[str]):
        url = "{0}/{1}/component_mget?{2}={3}&components={4}".format(
            QueryMaker.BASE_URL,
            level.value,
            Levels.get_id_key(level),
            id,
            ','.join(list(map((lambda x: level.value+'/'+x), endpoints)))
        )
        response = requests.get(url, auth=(self.key, self.secret))
        response.raise_for_status()
        return response.json()
