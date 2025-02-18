from src.model.configs.connection import DBConnectionHandler
from src.model.entities.events import Events

class EventsRepository:
    def insert(self, event_name: str) -> None:
        with DBConnectionHandler() as connection:
            try:
                new_event = Events(nome=event_name)
                connection.session.add(new_event)
                connection.session.commit()
            except Exception as exception:
                connection.session.rollback()
                raise exception

    def select_event(self, event_name: str) -> Events:
        with DBConnectionHandler() as connection:
            data = (
                connection.session
                .query(Events)
                .filter(Events.nome == event_name)
                .one_or_none()
            )
            return data