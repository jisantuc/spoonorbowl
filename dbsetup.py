import re
from sqlalchemy import (
    create_engine, Column, Integer, String, DateTime, Boolean,
    func
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///votes.db')
Session = sessionmaker(bind=engine)

class Vote(Base):
    __tablename__ = 'vote'

    id = Column(Integer, primary_key=True)
    image = Column(String)
    value = Column(Integer)

    @property
    def imagename(self):
        return re.sub(
            r'(\.jpg|\.png|\.gif)$',
            '',
            self.image
        )

    def __repr__(self):
        return (
            '<image: {image}, value: {value}>'.format(
                image=self.image, value=self.value
            )
        )


    def mean(self, image):
        sess = Session()
        vote = (sess.query(func.avg(Vote.value))
                .filter(Vote.image == image)
                .scalar())
        return round(vote, 2)

    @classmethod
    def add(cls, image_file, score):
        to_add = Vote(image=image_file, value=score)
        sess = Session()
        sess.add(to_add)
        sess.commit()
        sess.close()
        return to_add


if __name__ == '__main__':
    Base.metadata.create_all(engine)
