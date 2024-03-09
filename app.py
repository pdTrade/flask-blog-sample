from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from models import Entry

@app.route('/')
def show_entries():
  if not session.get('logged_in'):
    return redirect('/login')
  entries = Entry.query.order_by(Entry.id.desc()).all()
  return render_template('index.html', entries=entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if request.form['username'] != app.config['USERNAME']:
      flash('ユーザー名が間違っています')
    elif request.form['password'] != app.config['PASSWORD']:
      flash('ユーザー名が間違っています')
    else:
      session['logged_in'] = True
      flash('ログインしました')
      return redirect('/')

  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('ログアウトしました')
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)

@app.route('/entries/new')
def new_entry():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  return render_template('new.html')

@app.route('/entries', methods=['POST'])
def add_entry():
  if not session.get('logged_in'):
    return redirect(url_for('login'))

  entry = Entry(
    title=request.form['title'],
    text=request.form['text']
  )

  db.session.add(entry)
  db.session.commit()

  flash('記事が追加されました')

  return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>')
def show_entry(id):
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  entry = Entry.query.get(id)
  return render_template('show.html', entry=entry)

@app.route('/entries/<int:id>/edit')
def edit_entry(id):
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  entry = Entry.query.get(id)
  return render_template('edit.html', entry=entry)

@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  entry = Entry.query.get(id)
  entry.title = request.form['title']
  entry.text = request.form['text']

  db.session.merge(entry)
  db.session.commit()

  flash('記事が更新されました')

  return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  entry = Entry.query.get(id)

  db.session.delete(entry)
  db.session.commit()

  flash('記事が削除されました')

  return redirect(url_for('show_entries'))


# app.logger.debug(app.config['USERNAME'])
# app.logger.debug(app.config['PASSWORD'])
