from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


def now_plus_24_hours():
    return datetime.utcnow() + timedelta(hours=24)


class User(Base):
    __tablename__ = "tb_user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    celphone = Column(String)
    email = Column(String)
    document_number = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class PictureModel(Base):
    __tablename__ = "tb_picture"
    id = Column(Integer, primary_key=True, index=True)
    s3_link = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class AnimalLocationModel(Base):
    __tablename__ = "tb_animal_location_model"
    id = Column(Integer, primary_key=True, index=True)
    id_picture = Column(Integer, ForeignKey("tb_picture.id"))
    picture = relationship("PictureModel")
    description = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    expires_at = Column(DateTime, nullable=False, default=now_plus_24_hours)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class Animal(Base):
    __tablename__ = "tb_animal"
    id = Column(Integer, primary_key=True, index=True)
    id_picture = Column(Integer, ForeignKey("tb_picture.id"))
    picture = relationship("PictureModel")
    name = Column(String)
    specie = Column(String)
    birth_date = Column(DateTime)
    description = Column(String)
    city = Column(String)
    address = Column(String)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class UserAnimal(Base):
    __tablename__ = "tb_user_animal"
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("tb_user.id"))
    id_animal = Column(Integer, ForeignKey("tb_animal.id"))
    user = relationship("User")
    animal = relationship("Animal")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
