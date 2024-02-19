from flask import Flask
from .extensions import api,db
from .routes import ns, ns_user,ns_application,ns_category,ns_company,ns_listing,ns_review

def create_app():
    app = Flask(__name__)
    # app.run(debug=True)
    
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api.init_app(app)
    api.add_namespace(ns)
    api.add_namespace(ns_user)
    api.add_namespace(ns_company)
    api.add_namespace(ns_listing)
    api.add_namespace(ns_category)
    api.add_namespace(ns_application)
    api.add_namespace(ns_review)

    with app.app_context():
        # Create database tables
        db.create_all()

    return app
