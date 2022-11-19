club_name = "Simply Lift"
competition_name = "Spring Festival"


def test_club_should_not_book_more_than_12_places_one_pass(client):
    booked = 13
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


def test_club_book_less_than_12_places(client, expected_status_code=200):
    booked = 2
    response = client.post(
        '/purchasePlaces',
        data={
            'places': booked,
            'club': club_name,
            'competition': competition_name
        },
        follow_redirects=True
    )

    assert response.status_code == expected_status_code
    