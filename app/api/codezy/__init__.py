"""Here, Binding of end point goes on"""

from flask import Blueprint

from flask_restful import Api

from app.api.codezy.views import PostQuestion


stack = Blueprint("handle", __name__)

api = Api(stack)

api.add_resource(PostQuestion, '/api/v1/questions')