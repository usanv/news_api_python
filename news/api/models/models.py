from news.db.databse import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Time
from sqlalchemy.orm import relationship


# class Users(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     fullname = Column(String)
#     phone = Column(Integer)
#     username = Column(String(length=10))
#     password_hash = Column(String)
#     info = Column(String(length=250))


class NewsCategory(Base):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String)


class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(Text)
    published_at = Column(Time)
    photo = Column(String)
    news_category_id = Column(Integer, ForeignKey('news_category.id'))
    # news_category = relationship('News')
    # category = relationship('NewsCategory', back_populates='news')
