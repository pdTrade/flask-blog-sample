from app import app, db

class Entry(db.Model):
  __tablename__ = 'entries'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), unique=True)
  text = db.Column(db.Text)

  def __init__(self, title=None, text=None):
    self.title = title
    self.text = text

with app.app_context():
    db.create_all()
