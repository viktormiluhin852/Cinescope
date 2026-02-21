import requests
from tests.constants import BASE_URL, HEADERS

class TestBooking():

    def test_post_booking(self, auth_session, post_data, auth_session1):

        response = auth_session.post(f"{BASE_URL}/booking", json=post_data)

        assert response.status_code == 200
        resp_id = response.json().get("bookingid")
        assert resp_id is not None
        assert post_data.get("lastname") == response.json().get("booking").get("lastname")

        response = auth_session.get(f"{BASE_URL}/booking/{resp_id}", json=post_data)

        assert response.status_code == 200
        assert post_data.get("lastname") == response.json().get("lastname")

        response = requests.delete(f"{BASE_URL}/booking/{resp_id}", json=post_data, headers=HEADERS)
        assert response.status_code == 403

        response = auth_session1.delete(f"{BASE_URL}/booking/{resp_id}", json=post_data)
        assert response.status_code == 403

        response = auth_session.delete(f"{BASE_URL}/booking/{resp_id}", json=post_data)
        assert response.status_code == 201

        response = auth_session.get(f"{BASE_URL}/booking/{resp_id}", json=post_data)
        assert response.status_code == 404

    def test_put_booking(self, auth_session, auth_session1, post_data, put_data):

        response = auth_session.post(f"{BASE_URL}/booking", json=post_data)

        assert response.status_code == 200
        resp_id = response.json().get("bookingid")
        assert resp_id is not None
        assert post_data.get("lastname") == response.json().get("booking").get("lastname")

        response = auth_session.put(f"{BASE_URL}/booking/{resp_id}", json=put_data)
        assert response.status_code == 200
        assert put_data.get("lastname") == response.json().get("lastname")
        # Типо туут прям все поля проверили

        response = auth_session.get(f"{BASE_URL}/booking/{resp_id}")

        assert response.status_code == 200
        assert put_data.get("lastname") == response.json().get("lastname")
        # Типо туут прям все поля проверили

        def test_put_booking(self, auth_session, auth_session1, post_data, put_data):
            response = auth_session.post(f"{BASE_URL}/booking", json=post_data)

            assert response.status_code == 200
            resp_id = response.json().get("bookingid")
            assert resp_id is not None
            assert post_data.get("lastname") == response.json().get("booking").get("lastname")

            response = auth_session.put(f"{BASE_URL}/booking/{resp_id}", json=put_data)
            assert response.status_code == 200
            assert put_data.get("lastname") == response.json().get("lastname")

            response = auth_session.get(f"{BASE_URL}/booking/{resp_id}")

            assert response.status_code == 200
            assert put_data.get("lastname") == response.json().get("lastname")









