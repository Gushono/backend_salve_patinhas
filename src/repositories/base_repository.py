from fastapi_sqlalchemy import db


class BaseRepository:
    def __init__(self, model):
        self.model = model
        self.db = db

    @staticmethod
    def create(model, commit=True):
        db.session.add(model)

        if commit:
            db.session.commit()

        print(model)

        return model

    def get_all(self):
        return db.session.query(self.model).all()
