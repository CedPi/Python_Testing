club_name = "Simply Lift"


def test_club_should_not_book_past_competition(client):
    competition_name = "Fall Classic"
    url = f"/book/{competition_name}/{club_name}"
    response = client.get(url)

    assert response.status_code == 403


def test_club_should_book_past_competition(client):
    competition_name = "Spring Festival"
    url = f"/book/{competition_name}/{club_name}"
    response = client.get(url)

    assert response.status_code == 200