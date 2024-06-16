from app import app as flask_app
import unittest

class FlastTest(unittest.TestCase):

    def test_req_gpt_request(self):
        tester = flask_app.test_client(self)
        response = tester.post("/gpt", json={'message': 'hello gpt'})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    def test_req_gpt_empty_message(self):
        tester = flask_app.test_client(self)
        response = tester.post("/gpt", json={})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    
    def test_req_gpt_content(self):
        tester = flask_app.test_client(self)
        response = tester.post("/gpt", json={'message': 'hello gpt'})
        self.assertEqual(response.content_type, 'application/json')

if __name__ == "__main__":
    unittest.main()