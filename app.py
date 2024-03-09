from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def show_entries():
  return render_template('index.html')

@app.route('/login')
def login():
  return render_template('login.html')


if __name__ == '__main__':
  app.run(debug=True)



# app.logger.debug(app.config['USERNAME'])
# app.logger.debug(app.config['PASSWORD'])