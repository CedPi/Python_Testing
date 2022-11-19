def test_access_dashboard(client):
    response = client.get('/dashboard')
    assert response.status_code == 200