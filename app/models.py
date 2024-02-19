from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    location = db.Column(db.String(100))

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    location = db.Column(db.String(100))
    description = db.Column(db.String(100))

class JobCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class JobType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text)

class JobListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100))
    application_deadline = db.Column(db.DateTime, nullable=False)
    is_featured = db.Column(db.Boolean)
    
    employer_company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=True)
    employer_company = db.relationship('Company', backref=db.backref('jobs', lazy=True))
    
    category_id = db.Column(db.Integer, db.ForeignKey('job_category.id'), nullable=False)
    category = db.relationship('JobCategory', backref=db.backref('jobs', lazy=True))
    
    job_type_id = db.Column(db.Integer, db.ForeignKey('job_type.id'), nullable=False)
    job_type = db.relationship('JobType', backref=db.backref('jobs', lazy=True))

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job_listing.id'), nullable=False)
    job = db.relationship('JobListing', backref=db.backref('applications', lazy=True))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('applications', lazy=True))
    
    applicant_name = db.Column(db.String(100))
    applicant_email = db.Column(db.String(100))
    cover_letter = db.Column(db.Text)
    application_date = db.Column(db.DateTime, default=db.func.current_timestamp())

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship('Company', backref=db.backref('reviews', lazy=True))
    
    reviewer_name = db.Column(db.String(100))
    review_text = db.Column(db.Text)
    rating = db.Column(db.Integer)
    review_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))

