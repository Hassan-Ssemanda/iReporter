import pytest, json
from ireporter import create_app

def test_index(client):
    response = client.get('/')
    assert b"IReporter" in response.data
    assert b"On this platform any one can bring any form of corruption or anythning that requires intervation of authorities and the general public." in response.data