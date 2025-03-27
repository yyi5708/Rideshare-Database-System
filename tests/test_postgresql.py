import unittest
from src.rideshare import *
from src.rideshare_api import *
from src.swen344_db_utils import *
import unittest
from src.rideshare import *
from src.rideshare_api import *
from src.swen344_db_utils import *

class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):

        result = exec_get_one('SELECT VERSION()')
        self.assertTrue(result[0].startswith('PostgreSQL'))