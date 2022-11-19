from json import load
from flask import Flask
import pytest

import server


PLACE_PRICE= 3


@pytest.fixture
def client():

    with server.app.test_client() as client:
        yield client
        server.clubs = server.loadClubs()
        server.competitions = server.loadCompetitions()
        