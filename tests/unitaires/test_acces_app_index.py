def test_access_app(client):
    response = client.get('/')
    assert response.status_code == 200