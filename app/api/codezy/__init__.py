"""Here, Binding of end point goes on"""

from flask import Blueprint

from flask_restful import Api

from app.api.codezy.views import PostQuestion, PullQuestions, \
    PullSingleQuestions, Answer


stack = Blueprint("handle", __name__)

api = Api(stack)

api.add_resource(PostQuestion, '/api/v1/questions')
api.add_resource(PullQuestions, '/api/v1/questions')
api.add_resource(PullSingleQuestions, '/api/v1/questions/<questionId>')
api.add_resource(Answer, '/api/v1/questions/<questionId>/answers')
