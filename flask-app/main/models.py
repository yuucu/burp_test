from main import db
from flask_sqlalchemy import SQLAlchemy


class Comment(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.Text)

  def __repr__(self):
    return "<Comment id={} text={!r}>".format(self.id, self.text)

def init():
  db.create_all()
