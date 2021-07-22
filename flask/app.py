from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Requires Credentials, Endpoint, Port and Database name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://[credentials]@[endpoint]:[port][database name]'

class Orders(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	pizza = db.Column(db.String(30), nullable=False)
	size = db.Column(db.Integer, nullable=False)
	customer = db.Column(db.String(150), nullable=False)
	cost = db.Column(db.Integer, nullable=False)
	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 'Pizza: ', self.pizza, 'Customer: ', self.customer])


@app.route('/')
def hello():
  data1 = Orders.query.all()
  return render_template('home.html', data1=data1)

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
