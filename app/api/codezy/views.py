"""Views module."""

from flask_restful import Resource

from flask import request

from app.api.codezy.model import Data

from app.api.codezy.helper import GreatHelper


class PostQuestion(Resource, Data):

    def __init__(self):
        self.obj = GreatHelper()

    def post(self):
        """Post question here"""

        if request.content_type == 'application/json':
            info = request.get_json()
            if info != '':
                question = info["msg"]
                result = self.store_question(question)
                if result:
                    return self.obj.response("Successful", "Successfully posted")
            return self.obj.response("Failed", "Sorry, can't post this question")