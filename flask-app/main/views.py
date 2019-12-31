import flask
import uuid
from flask import session, redirect, url_for, Markup
from main import app, db
from main.models import Comment


@app.route('/')
def index():
  comments = Comment.query.all()
  return flask.render_template('index.html', comments=comments)


@app.route('/add_comment', methods=['POST'])
def add_comment():
  text = flask.request.form['text']
  if text == '':
    pass
  else:
    comment = Comment(
      text = text
    )
    db.session.add(comment)
    db.session.commit()
  return flask.redirect(url_for('index'))


@app.route('/data_reset')
def data_reset():
  try:
    delete_row_num = Comment.query.delete()
    db.session.commit()
  except:
    db.session.rollback()
  return redirect(url_for('index'))
