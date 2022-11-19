def test_email_should_connect(client):
    email = 'admin@irontemple.com'
    response = client.post('/showSummary', data={'email': email}, follow_redirects=True)
    assert response.status_code == 200


def test_email_should_fail(client):
    email = 'dummy@test.com'
    response = client.post('/showSummary', data={'email': email}, follow_redirects=True)
    assert response.status_code == 403


def test_email_is_empty(client):
    email = ''
    response = client.post('/showSummary', data={'email': email}, follow_redirects=True)
    assert response.status_code == 403