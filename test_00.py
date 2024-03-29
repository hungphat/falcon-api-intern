from falcon import testing
from app import *
import json


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now

db = data_base
class Test(testing.TestCase):

    def setUp(self):
       sql ="DROP TABLE IF EXISTS customers"
       db.session.execute(sql)


    def test_001a(self):
        pass
       # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api

    def test_00(self):
        body =[
            {
                "id": 1,
                "name": "Name01",
                "dob": "2018-01-02",
                "updated_at": "2019-08-12 04:05:01"
            },
            {
                "id": 2,
                "name": "Name02",
                "dob": "2018-02-03",
                "updated_at": "2019-08-13 04:05:01"
            },
            {
                "id": 3,
                "name": "Name03",
                "dob": "2018-03-04",
                "updated_at": "2019-08-14 04:05:01"
            },
            {
                "id": 4,
                "name": "Name04",
                "dob": "2018-04-05",
                "updated_at": "2019-08-15 04:05:01"
            },
            {
                "id": 5,
                "name": "Name05",
                "dob": "2018-05-06",
                "updated_at": "2019-08-16 04:05:01"
            },
        ]
        r = self.simulate_get(f'/customers/')
        assert r.status_code == 200
        assert r.json == body

    def test_00a(self):
        r = self.simulate_get(f'/customers/1')
        assert r.status_code == 200


    def test_01(self):
        body = {
            "id": 1,
            "name": "Name01",
            "dob": "2018-01-02",
            "updated_at": "2019-08-12 17:11:58.563520"
        }
        r = self.simulate_get(f'/customers/1')
        assert r.status_code == 200
        assert r.json == body

    def test_02(self):
        body = {
                "name" :  "thang",
                "dob"  : "2018-10-10",
        }
        d = {
            "id": "6"
        }
        expected_out = json.dumps(d)
        r = self.simulate_post(f'/customers/', body=json.dumps(body))
        assert r.status_code == 200
        assert r.text == expected_out

    def test_03(self):
        body = {
            "dob": "1993-9-9"
        }
        r = self.simulate_put(f'/customers/6', body=json.dumps(body))
        assert r.status_code == 200

    def test_04(self):
        input_delete = 6
        body = {
            "id" : input_delete
        }
        r = self.simulate_delete(f'/customers/{input_delete}')
        assert r.status_code == 200







