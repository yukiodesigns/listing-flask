from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restx import Namespace, Resource, reqparse
from .models import User, JobListing, JobCategory, JobType, Company, Application, Review
from .api_models import user_model, user_input_model, company_model, company_input_model,category_model, category_input_model,job_type_model,job_type_input_model,listing_model,listing_input_model,application_model,application_input_model,review_model,review_input_model
from .extensions import db
from datetime import datetime
ns=Namespace('job_type', description='Job Type operations')

ns_user = Namespace('user', description='User operations')
ns_company = Namespace('company', description='Company operations')
ns_listing = Namespace('listing', description='Listing operations')
ns_category = Namespace('category', description='Category operations')
ns_application = Namespace('application', description='Application operations')
ns_review = Namespace('review', description='Review operations')


user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True, help='User name')
user_parser.add_argument('email', type=str, required=True, help='User email')
user_parser.add_argument('password', type=str, required=True, help='User password')
user_parser.add_argument('location', type=str, required=True, help='User location')

# password_parser = reqparse.RequestParser()
# password_parser.add_argument('password', type=str, required=True, help='New password')

@ns_user.route('/')
class UserList(Resource):
    @ns_user.marshal_list_with(user_model)
    def get(self):
        return User.query.all()

    @ns_user.expect(user_parser)
    @ns_user.marshal_with(user_model)
    def post(self):
        args = user_parser.parse_args()
        hashed_password = generate_password_hash(args['password'])
        new_user = User(name=args['name'],email=args['email'],password=hashed_password,location = args['location'])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201  

@ns_user.route('/<int:id>')
class UserAPI(Resource):
    @ns_user.marshal_with(user_model)
    def get(self, id):
        return User.query.get(id)
    
    @ns_user.expect(user_parser)
    @ns_user.marshal_with(user_model)
    def put(self, id):
        user = User.query.get(id)
        user.name = request.json['name']
        user.email = request.json['email']
        user.location = request.json['location']
        db.session.commit()
        return user, 200

    # @ns_user.expect(password_parser, validate=True)
    # @ns_user.marshal_with(user_model)
    # def patch(self, id):
    #     user = User.query.get(id)
    #     new_password = request.json['password']

    #     hashed_password = generate_password_hash(new_password)
    #     user.password = hashed_password

    #     db.session.commit()
    #     return user, 200
    
    @ns.expect(user_input_model)
    @ns.marshal_with(user_model)
    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user, 200
 
@ns_company.route('/')
class CompanyList(Resource):
    @ns.marshal_list_with(company_model)
    def get(self):
        return Company.query.all()
    
    @ns.expect(company_input_model)
    @ns.marshal_with(company_model)
    def post(self):
        company = Company.query.filter_by(email=request.json['email']).first()
        if company:
            return {'message':'Email already exists'}, 400
        company = Company(name=request.json['name'], email=request.json['email'], location=request.json['location'], description=request.json['description'])
        db.session.add(company)
        db.session.commit()
        return company, 201

@ns_company.route('/<int:id>')
class CompanyAPI(Resource):
    @ns.marshal_with(company_model)
    def get(self, id):
        return Company.query.get(id)
    
    @ns.expect(company_input_model)
    @ns.marshal_with(company_model)
    def put(self, id):
        company = Company.query.get(id)
        company.name = request.json['name']
        company.email = request.json['email']
        company.location = request.json['location']
        company.description = request.json['description']
        db.session.commit()
        return company, 200
    
    @ns.expect(company_input_model)
    @ns.marshal_with(company_model)
    def delete(self, id):
        company = Company.query.get(id)
        db.session.delete(company)
        db.session.commit()
        return {}, 204

@ns_listing.route('/')
class ListingList(Resource):
    @ns.marshal_list_with(listing_model)
    def get(self):
        return JobListing.query.all()
    
    @ns.expect(listing_input_model)
    @ns.marshal_list_with(listing_model)
    def post(self):
        listing = JobListing(title=request.json['title'], description=request.json['description'], requirements=request.json['requirements'], date_posted=datetime.strptime(request.json['date_posted'], '%Y-%m-%d'), location=request.json['location'], application_deadline=datetime.strptime(request.json['application_deadline'], '%Y-%m-%d'),is_featured=request.json['is_featured'], employer_company_id=request.json['employer_company_id'], category_id=request.json['category_id'],job_type_id=request.json['job_type_id'])
        db.session.add(listing)
        db.session.commit()
        return listing, 201

@ns_listing.route('/<int:id>')
class ListingAPI(Resource):
    @ns.marshal_list_with(listing_model)
    def get(self, id):
        return JobListing.query.get(id)
    
    @ns.expect(listing_input_model)
    @ns.marshal_with(listing_model)
    def put(self, id):
        listing = JobListing.query.get(id)
        listing.title = request.json['title']
        listing.description = request.json['description']
        listing.requirements = request.json['requirements']
        listing.location = request.json['location']
        listing.application_deadline = datetime.strptime(request.json['application_deadline'], '%Y-%m-%d')
        listing.is_featured = request.json['is_featured']
        db.session.commit()
        return listing, 200
    
    @ns.expect(listing_input_model)
    @ns.marshal_list_with(listing_model)
    def delete(self, id):
        listing = JobListing.query.get(id)
        db.session.delete(listing)
        db.session.commit
        return {}, 204

@ns_category.route('/')
class CategoryList(Resource):
    @ns.marshal_list_with(category_model)
    def get(self):
        return JobCategory.query.all()
    
    @ns.expect(category_input_model)
    @ns.marshal_list_with(category_model)
    def post(self):
        category = JobCategory(name=request.json['name'])
        db.session.add(category)
        db.session.commit()
        return category, 201

@ns_category.route('<int:id>')
class CategoryAPI(Resource):
    @ns.marshal_list_with(category_model)
    def get(self, id):
        return JobCategory.query.get(id)
    
    @ns.expect(category_input_model)
    @ns.marshal_list_with(category_model)
    def put(self,id):
        category = JobCategory.query.get(id)
        category.name = request.json['name']
        db.session.commit()
        return category, 200
    
    @ns.expect(category_input_model)
    @ns.marshal_list_with(category_model)
    def delete(self, id):
        category = JobCategory.query.get(id)
        db.session.delete(category)
        db.session.commit()
        return {}, 204
    
@ns.route('/job_type')
class JobTypeList(Resource):
    @ns.marshal_list_with(job_type_model)
    def get(self):
        return JobType.query.all()
    
    @ns.expect(job_type_input_model)
    @ns.marshal_list_with(job_type_model)
    def post(self):
        job_type = JobType(name=request.json['name'], description=request.json['description'])
        db.session.add(job_type)
        db.session.commit()
        return job_type, 201

@ns.route('/job_type/<int:id>')
class JobTypeAPI(Resource):
    @ns.marshal_list_with(job_type_model)
    def get(self,id):
        return JobType.query.get(id)

    @ns.expect(job_type_input_model)
    @ns.marshal_list_with(job_type_model)
    def put(self,id):
        job_type = JobType.query.get(id)
        job_type.name = request.json['name']
        db.session.commit()
        return job_type, 200

    @ns.expect(job_type_input_model)
    @ns.marshal_list_with(job_type_model)
    def delete(self, id):
        job_type = JobType.query.get(id)
        db.session.delete(job_type)
        db.session.commit()
        return {}, 204  
     
@ns_application.route('/')
class ApplicationList(Resource):
    @ns.marshal_list_with(application_model)
    def get(self):
        return Application.query.all()
    
    @ns.expect(application_input_model)
    @ns.marshal_list_with(application_model)
    def post(self):
        application = Application(job_id=request.json['job_id'],  user_id=request.json['user_id'], application_date=datetime.strptime(request.json['application_date'], '%Y-%m-%d') , applicant_name=request.json['applicant_name'],applicant_email=request.json['applicant_email'],cover_letter=request.json['cover_letter'])
        db.session.add(application)
        db.session.commit()
        return application, 201    

@ns_application.route('/<int:id>')
class ApplicationAPI(Resource):
    @ns.marshal_list_with(application_model)
    def get(self, id):
        return Application.query.get(id)
    
    @ns.expect(application_input_model)
    @ns.marshal_list_with(application_model)
    def put(self,id):
        application = Application.query.get(id)
        application.company_id = request.json['company_id']
        application.job_listing_id = request.json['job_listing_id']
        application.user_id = request.json['user_id']
        application.application_date = datetime.strptime(request.json['application_date'], '%Y-%m-%d')
        db.session.commit()
        return application, 200
    
    @ns.expect(application_input_model)
    @ns.marshal_list_with(application_model)
    def delete(self, id):
        application = Application.query.get(id)
        db.session.delete(application)
        db.session.commit()
        return {}, 204
    
@ns_review.route('/')
class ReviewList(Resource):
    @ns.marshal_list_with(review_model)
    def get(self):
        return Review.query.all()
    
    @ns.expect(review_input_model)
    @ns.marshal_list_with(review_model)
    def post(self):
        review = Review(company_id=request.json['company_id'] ,review_date=datetime.strptime(request.json['review_date'], '%Y-%m-%d'), user_id=request.json['user_id'], rating=request.json['rating'],reviewer_name=request.json['reviewer_name'],review_text=request.json['review_text'])
        db.session.add(review)
        db.session.commit()
        return review, 201
    
@ns_review.route('/<int:id>')
class ReviewAPI(Resource):
    @ns.marshal_list_with(review_model)
    def get(self, id):
        return Review.query.get(id)
    
    @ns.expect(review_input_model)
    @ns.marshal_list_with(review_model)
    def put(self,id):
        review = Review.query.get(id)
        review.user_id = request.json['user_id']
        review.rating = request.json['rating']
        review.company_id = request.json['company_id'] 
        review.review_date=datetime.strptime(request.json['review_date'], '%Y-%m-%d')
        review.reviewer_name=request.json['reviewer_name']
        review.review_text=request.json['review_text']
        db.session.commit()
        return review, 200
    
    @ns.expect(review_input_model)
    @ns.marshal_list_with(review_model)
    def delete(self, id):
        review = Review.query.get(id)
        db.session.delete(review)
        db.session.commit()
        return {}, 204