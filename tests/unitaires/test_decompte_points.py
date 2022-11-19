club_name = "Simply Lift"
club_points = 13
competition_name = "Spring Festival"
booked_places = 2

def test_club_point_should_substract(client):
    response = client.post(
        '/purchasePlaces',
        data={
            'places': booked_places,
            'club': club_name,
            'competition': competition_name
        },
        follow_redirects=True
    )

    expected_data = str('Points available: ' + str(club_points - booked_places))
    data = response.data.decode()
    
    assert response.status_code == 200
    assert data.find(expected_data) != -1