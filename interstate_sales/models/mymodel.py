from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    category = Column(Text)
    subcategory = Column(Text)
    title = Column(Text)
    img = Column(Text)
    markdown = Column(Text)
    extra = Column(Text)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
