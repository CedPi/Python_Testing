club_name = "Simply Lift"
competition_name = "Spring Festival"


def test_club_should_not_book_more_than_points(client):
    booked_places = 15

    response = client.post(
        '/purchasePlaces',
        data={
            'places': booked_places,
            'club': club_name,
            'competition': competition_name
        },
        follow_redirects=True
    )

    assert response.status_code == 400


def test_club_book_should_be_ok(client):
    booked_places = 3

    response = client.post(
        '/purchasePlaces',
        data={
            'places': booked_places,
            'club': club_name,
            'competition': competition_name
        },
        follow_redirects=True
    )

    assert response.status_code == 200