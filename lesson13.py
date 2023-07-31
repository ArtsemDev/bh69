from datetime import datetime
from typing import Any

from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    ForeignKey,
    TIMESTAMP,
    TEXT,
    create_engine,
    CheckConstraint,
    select,
    update,
    delete,
    and_,
    any_,
    all_,
    or_
)
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker, declared_attr, Session
from sqlalchemy.sql.functions import count

from pydantic import BaseModel, PositiveInt, Field, PostgresDsn, ConfigDict
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()

# from sqlalchemy.orm import declarative_base
# DeclarativeBase - sqlalchemy > 2
# declarative_base - sqlalchemy < 2


# Base = declarative_base()


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn


SETTINGS = Settings()


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    engine = create_engine(url=SETTINGS.DATABASE_URL.unicode_string())
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    def from_attributes(self, obj: Any):
        for k, v in obj.__dict__.items():
            if hasattr(self, k):
                setattr(self, k, v)


class Category(Base):
    __table_args__ = (
        CheckConstraint('char_length(name) >= 4'),
    )

    name = Column(VARCHAR(64), nullable=False, unique=True)

    posts = relationship(argument='Post', back_populates='category')

    def __repr__(self):
        return self.name


class Post(Base):
    title = Column(VARCHAR(128), nullable=False)
    descr = Column(TEXT, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())
    date_updated = Column(TIMESTAMP, onupdate=datetime.utcnow())
    category_id = Column(INT, ForeignKey(column='category.id', ondelete='RESTRICT'), nullable=False)

    category = relationship(argument='Category', back_populates='posts')

    def __repr__(self):
        return self.title


# Base.metadata.create_all(bind=Base.engine)
# Base.metadata.drop_all(bind=Base.engine)


# with Base.session() as session:  # type: Session
#     category1 = Category(name='Coffee')
#     category2 = Category(name='Pancake')
#     session.add_all((category1, category2))
#     session.commit()
#     session.refresh(category1)
#     session.refresh(category2)
#     print(category1.id, category2.id)

# with Base.session() as session:
    # objs = session.execute()  # используется для UPDATE, DELETE, JOIN, UNION
    # objs = session.scalars()  # используется для SELECT
    # obj = session.scalar()  # используется для SELECT
    # category1 = session.get(Category, 6)
    # category1.name = 'Кофе'
    # session.commit()
    # objs = session.scalars(
    #     select(Category)
    #     .order_by(Category.name.desc())
    #     .filter(Category.id.in_([6, 7]))
    #     # .limit(2)
    #     # .offset(3)
    # )
    # objs = objs.all()
    # print(objs[0].posts)
    # objs = session.execute(
    #     select(Category, Post)
    #     .join(Post, isouter=True)
    # )
    # print(objs.all())


# with Category.session() as session:
#     session.execute(
#         update(Category)
#         .filter_by(name='Кофе')
#         .values(name='Coffee')
#     )
#     session.commit()


# with Category.session() as session:
#     session.execute(
#         delete(Category)
#         .filter(or_(Category.id > 10, Category.id < 5))
#     )
#     session.commit()


# with Category.session() as session:
#     c = session.scalar(select(count(Category.id)))
#     print(c)


class PostSchema(BaseModel):
    id: PositiveInt
    title: str
    descr: str
    date_created: datetime
    date_updated: datetime
    category_id: PositiveInt


class CategorySchema(BaseModel):
    id: PositiveInt
    name: str = Field(..., min_length=4, max_length=64)

    posts: list[PostSchema]

    # class Config:
    #     orm_mode = True  # добавляет метод класса from_orm в pydantic < 2


# schema = CategorySchema(id=1, name='Coffee')

# print(schema.model_dump())
# with Category.session() as session:
#     obj = session.get(Category, schema.id)
#     obj.from_attributes(obj=schema)
#     session.commit()


# with Post.session() as session:
    # post = Post(title='Title1', descr='Description', category_id=1)
    # session.add(post)
    # session.commit()
    # session.refresh(post)
    # print(post.__dict__)
    # post = session.get(Post, 1)
    # post.title = 'Title 1'
    # session.commit()
    # session.refresh(post)
    # print(post.__dict__)
    # c = session.get(Category, 1)
    # print(c.posts[0].category)


with Category.session() as session:
    c = session.get(Category, 1)
    print(CategorySchema.model_validate(c, from_attributes=True).model_dump_json())
