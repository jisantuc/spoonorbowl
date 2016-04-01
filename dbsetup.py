import re
from sqlalchemy import (
    create_engine, Column, Integer, String, DateTime, Boolean
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Vote(Base):
    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    image = Column(String)
    value = Column(Integer)

    @property
    def filename(self):
        return re.sub(
            r'(\.jpg|\.png|\.gif)$',
            '',
            self.image
        )

    def __repr__(self):
        return (
            '<image: {image} value: {value}>'.format(
                image=self.filename, value=self.value
            )
        )

engine = create_engine('sqlite:///votes.db')
Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
