def test_deconnexion(client):
    response = client.get('/logout')
    assert response.status_code == 302