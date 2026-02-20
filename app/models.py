from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    registry,
)

table_registry = registry()


class Base(declarative_base): ...


class Assets(Base):
    __tablename__ = "assets"
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
