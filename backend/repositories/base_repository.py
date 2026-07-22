from typing import Generic, TypeVar

from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        db: Session,
        model: type[ModelType]
    ):
        self.db = db
        self.model = model

    def get_all(self):

        return (
            self.db
            .query(self.model)
            .all()
        )

    def get_by_id(
        self,
        object_id: int
    ):

        primary_key = list(
            self.model.__table__.primary_key.columns
        )[0]

        return (
            self.db
            .query(self.model)
            .filter(primary_key == object_id)
            .first()
        )

    def create(
        self,
        obj: ModelType
    ):

        self.db.add(obj)

        self.db.commit()

        self.db.refresh(obj)

        return obj

    def update(self):

        self.db.commit()

    def delete(self, obj):

        self.db.delete(obj)

        self.db.commit()