from urllib import response
from src.app import app
import unittest


class FlaskTest(unittest.TestCase):
    
    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    # Ensure that the the home page loads correctly
    def test_correct(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        statuscode = response.status_code
        self.assertTrue(b'City' in response.data)

    # Ensure that data is correctly saved to database
    def test_sensor(self):
        tester = app.test_client(self)
        response = tester.post('/add',data=dict(city='Paris',country='France'),follow_redirects=True)
        statuscode = response.status_code
        self.assertTrue(b'Add New Sensor' in response.data)


if __name__ == "__main__":
    unittest.main()