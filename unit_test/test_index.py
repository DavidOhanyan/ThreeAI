from app import app as flask_app
import unittest

class FlastTest(unittest.TestCase):
    
    def test_index(self):
        tester = flask_app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
if __name__ == "__main__":
    unittest.main()