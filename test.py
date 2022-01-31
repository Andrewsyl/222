from urllib import response
from flask import request
from src.app import app
import unittest

class FlaskTest(unittest.TestCase):
    
    # Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    # Ensure that the the home page loads correctly
    def test_homepage(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        self.assertTrue(b'City' in response.data)

    # Ensure that data is correctly saved to database
    def test_sensor_data(self):
        tester = app.test_client(self)
        response = tester.post('/add',data=dict(city='Paris',country='France'),follow_redirects=True)
        self.assertTrue(b'Add New Sensor' in response.data)

    # Ensure that getting sensor page works
    def test_sensor_page_post(self):
        tester = app.test_client(self)
        response = tester.post('/sensor_info/2',follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    # Ensure that query on sensor page works
    def test_sensor_page_get(self):
        tester = app.test_client(self)
        response = tester.get('/sensor_info/2',follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    


if __name__ == "__main__":
    unittest.main()