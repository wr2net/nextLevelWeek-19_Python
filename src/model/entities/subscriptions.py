from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Subscriptions(Base):
    __tablename__ = "Inscritos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    link = Column(String, nullable=False)
    evento_id = Column(Integer, ForeignKey("Eventos.id"))