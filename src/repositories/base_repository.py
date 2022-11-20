from fastapi_sqlalchemy import db


class BaseRepository:
    def __init__(self, model):
        self.model = model

    @staticmethod
    def create(model, commit=True):

        db.session.add(model)

        if commit:
            db.session.commit()

        return model

    def get_all(self, params=None):
        if params:
            return db.session.query(self.model).filter_by(**params).all()

        return db.session.query(self.model).all()
