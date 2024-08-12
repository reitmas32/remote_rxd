from sqlalchemy import Column, String

from models.base_model import BaseModelClass


class UserModel(BaseModelClass):
    __tablename__ = "user"
    __table_args__ = {"schema": "core"}  # noqa: RUF012

    email = Column(String, nullable=False)
    public_key = Column(String, nullable=False)

    def as_dict(self):
        return {"email": self.email.__str__()}
