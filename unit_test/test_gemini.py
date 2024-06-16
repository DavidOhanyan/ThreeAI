from app import app as flask_app
import unittest

class FlastTest(unittest.TestCase):

    def test_req_gemini_request(self):
        tester = flask_app.test_client(self)
        response = tester.post("/gemini", json={'message': 'hello gemini'})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_req_gemini_empty_message(self):
        tester = flask_app.test_client(self)
        response = tester.post("/gemini", json={})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    def test_req_gemini_content(self):
        tester = flask_app.test_client(self)
        response = tester.post("/gemini", json={'message': 'hello gemini'})
        self.assertEqual(response.content_type, 'application/json')

if __name__ == "__main__":
    unittest.main()