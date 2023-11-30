from datetime import datetime
from sqlalchemy.orm import relationship

from webapp.db import db



class News(db.Model):                                       # class News inheritans with .Model (DB SQLite)
    id = db.Column(db.Integer, primary_key=True)            # id news (number)
    title = db.Column(db.String, nullable=False)            # column title
    url = db.Column(db.String, unique=True, nullable=False) # column url
    published = db.Column(db.DateTime, nullable=False)      # column published
    text = db.Column(db.Text, nullable=True)                # text news (nullable=True -> None)

    def comments_count(self):
        return Comment.query.filter(Comment.news_id == self.id).count()

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)           # id comment
    text = db.Column(db.Text, nullable=False)               # text comment
    created = db.Column(db.DateTime, nullable=False, default=datetime.now()) # data comment
    
    # create id for news    
    news_id = db.Column(
        db.Integer,                                   # id - integer      
        db.ForeignKey('news.id', ondelete='CASCADE'), # id is ForeignKey, ondelete='CASCADE' - if you del news, to del comments; index=True - index need create  
        index=True
        )
    # create id for user
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
        )
    news = relationship('News', backref='comments')
    user = relationship('User', backref='comments')

    def __repr__(self):
        return '<Comment {}>'.format(self.id)