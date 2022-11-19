club_name = "Simply Lift"
competition_name = "Spring Festival"


def test_club_should_not_book_more_than_available(client):
    booked = 30
    response = client.post(
        '/purchasePlaces',
        data={
            'places': booked,
            'club': club_name,
            'competition': competition_name
        },
        follow_redirects=True
    )

    assert response.status_code == 400


def test_club_book_number_of_places_ok(client):
    booked = 5
    response = client.post(
        '/purchasePlaces',
        data={
            'places': booked,
            'club': club_name,
            'competition': competition_name
        },
        follow_redirects=True
    )

    assert response.status_code == 200