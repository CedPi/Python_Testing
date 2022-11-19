club_name = "Iron Temple"
competition_name = "Spring Festival"

fake_club = "Fake Club"
fake_competition = "Fake Competition"

fake_club_url = f"/book/{competition_name}/{fake_club}"
fake_competition_url = f"/book/{fake_competition}/{club_name}"


def test_book_with_unknown_club(client):
    response = client.get(fake_club_url)

    assert response.status_code == 403


def test_book_with_unknown_competition(client):
    response = client.get(fake_competition_url)

    assert response.status_code == 403