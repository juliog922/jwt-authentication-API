import unittest
from fastapi.testclient import TestClient
from api.main import app

class TestEndpoints(unittest.TestCase):
    """Class to test endpoints
    """    
    def setUp(self):
        """Test Client setup
        """        
        self.client = TestClient(app)
        self.test_user = {
            "email": "test@example.com",
            "password": "Testpassword",
        }

    def test_sign_in_and_logout_endpoints(self):
        """Sign in, Login and Logout tests.
        """        
        
        response = self.client.post("/sign_in", json=self.test_user)
        self.assertEqual(response.status_code, 200)

        
        login_data = {
            "username": self.test_user["email"],
            "password": self.test_user["password"]
        }
        response = self.client.post("/login", data=login_data)
        self.assertEqual(response.status_code, 200)
        token = response.json()["access_token"]

        
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.post("/logout", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "User checkout correctly.")


