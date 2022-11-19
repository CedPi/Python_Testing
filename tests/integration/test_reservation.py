import pytest
from tests.conftest import PLACE_PRICE


@pytest.fixture
def club_fixture():
    data = {
        "name":"Simply Lift",
        "email":"john@simplylift.co",
        "points":"13"
    }
    return data

@pytest.fixture
def competition_fixture():
    data = {
        "name": "Spring Festival",
        "date": "2023-03-27 10:00:00",
        "numberOfPlaces": "25"
    }
    return data


booked_places = 2


def test_reservation_route_ok(client, club_fixture, competition_fixture):
    response = client.post('/showSummary', data={'email': club_fixture['email']}, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert data.find(f"Welcome, {club_fixture['email']}") != -1

    response = client.post(
        '/purchasePlaces',
        data={
            'places': booked_places,
            'club': club_fixture['name'],
            'competition': competition_fixture['name']
        },
        follow_redirects=True
    )
    expected_club_data = str('Points available: ' + str(int(club_fixture['points']) - booked_places * PLACE_PRICE))
    expected_competition_name = str(f"{competition_fixture['name']}")
    expected_competition_date = f"Date: {competition_fixture['date']}"
    expected_competition_places = f"Number of Places: {int(competition_fixture['numberOfPlaces']) - booked_places}"
    data = response.data.decode()
    assert response.status_code == 200
    assert data.find(expected_club_data) != -1
    assert data.find(expected_competition_name) != -1
    assert data.find(expected_competition_date) != -1
    assert data.find(expected_competition_places) != -1

    response = client.get('/logout')
    assert response.status_code == 302
    
