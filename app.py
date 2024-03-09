from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def show_entries():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if request.form['username'] != app.config['USERNAME']:
      app.logger.debug('ユーザー名が間違っています')
    elif request.form['password'] != app.config['PASSWORD']:
      app.logger.debug('ユーザー名が間違っています')
    else:
      return redirect('/')

  return render_template('login.html')


if __name__ == '__main__':
  app.run(debug=True)



# app.logger.debug(app.config['USERNAME'])
# app.logger.debug(app.config['PASSWORD'])