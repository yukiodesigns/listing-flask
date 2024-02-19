from flask_restx import fields
from .extensions import api 

user_model = api.model('User',{
    "id":fields.Integer,
    "name":fields.String,
    "email":fields.String,
    "password":fields.String,
    "location":fields.String
})
company_model = api.model('Company',{
    "id":fields.Integer,
    "name":fields.String,
    "email":fields.String,
    "location":fields.String,
    "description":fields.String
})
category_model = api.model('JobCategory',{
    "id":fields.Integer,
    "name":fields.String
})
job_type_model = api.model('JobType',{
    "id":fields.Integer,
    "name":fields.String,
    "description":fields.String
})
listing_model = api.model('JobListing',{
    "id":fields.Integer,
    "title": fields.String,
    "description":fields.String,
    "requirements":fields.String,
    "date_posted":fields.DateTime,
    "location":fields.String,
    "is_featured":fields.Boolean,
    "application_deadline":fields.DateTime,
    "employer_company_id":fields.Integer,
    "category_id":fields.Integer,
    "job_type_id":fields.Integer,
    # "employer_company":fields.List(fields.Nested(company_model))
})
application_model = api.model('Application',{
    "id":fields.Integer,
    "job_id":fields.Integer,
    "user_id":fields.Integer,
    "applicant_name":fields.String,
    "applicant_email":fields.String,
    "cover_letter":fields.String,
    "application_date":fields.DateTime,
    # "job":fields.List(fields.Nested(listing_model)),
    # "user":fields.List(fields.Nested(user_model))

})
review_model = api.model('Reviews',{
    "id":fields.Integer,
    "company_id":fields.Integer,
    "reviewer_name":fields.String,
    "review_text":fields.String,
    "rating":fields.Integer,
    "review_date":fields.DateTime,
    "user_id":fields.Integer,
    # "user":fields.List(fields.Nested(user_model)),
    # "company":fields.List(fields.Nested(company_model))
})


# Input models
user_input_model = api.model('UserInput',{
    "name":fields.String,
    "email":fields.String,
    "password":fields.String,
    "location":fields.String
})
company_input_model = api.model('CompanyInput',{
    "name":fields.String,
    "email":fields.String,
    "location":fields.String,
    "description":fields.String
})
category_input_model = api.model('CategoryInput',{
    "name":fields.String
})
job_type_input_model = api.model('JobTypeInput',{
    "name":fields.String,
    "description":fields.String
})
listing_input_model = api.model('ListingInput',{
    "title": fields.String,
    "description":fields.String,
    "requirements":fields.String,
    "date_posted":fields.DateTime,
    "location":fields.String,
    "is_featured":fields.Boolean,
    "application_deadline":fields.DateTime,
    "employer_company_id":fields.Integer,
    "category_id":fields.Integer,
    "job_type_id":fields.Integer
})
application_input_model = api.model('ApplicationInput',{
    "job_id":fields.Integer,
    "user_id":fields.Integer,
    "applicant_name":fields.String,
    "applicant_email":fields.String,
    "cover_letter":fields.String,
    "application_date":fields.DateTime
})
review_input_model = api.model('ReviewInput',{
    "company_id":fields.Integer,
    "reviewer_name":fields.String,
    "review_text":fields.String,
    "rating":fields.Integer,
    "review_date":fields.DateTime
})

# student_input_model = api.model('StudentInput',{
#     "name":fields.String,
#     "course_id":fields.Integer
# })