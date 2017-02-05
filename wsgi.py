from config import Config
from flask_template import create_app, create_worker, register_celery

app = create_app(Config(
    bootstrap=True,
    db='mysql+mysqlconnector://'
       'flask-template:flask-template'
       '@jxltom.me:3306/flask-template',
    scheduler=True,
    mail=True,
    index=True,
    login=True,
    wechat=True,
))
worker = create_worker(app)
register_celery()

if __name__ == '__main__':
    app.config.update(DEBUG=True)
    app.run()
