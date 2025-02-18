import pytest
from .events_repository import EventsRepository

@pytest.mark.skip("Insert in DB")
def test_insert_events():
    event_name = "eventoTeste"
    event_repo = EventsRepository()
    event_repo.insert(event_name)

@pytest.mark.skip("Select in DB")
def test_selec_event():
    event_name = "eventoTeste"
    event_repo = EventsRepository()
    event_repo.select_event(event_name)

