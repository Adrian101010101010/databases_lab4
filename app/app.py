from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_CONFIG


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}:{port}/{database}'.format(
    user=DB_CONFIG['user'],
    password=DB_CONFIG['password'],
    host=DB_CONFIG['host'],
    port=DB_CONFIG['port'],
    database=DB_CONFIG['database']
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
