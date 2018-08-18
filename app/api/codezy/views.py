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

class PullQuestions(Resource, Data, GreatHelper):
    """Here all questions can be viewed. """

    def get(self):
        content = self.cont
        return self.response("Questions", content)


class PullSingleQuestions(Resource, Data, GreatHelper):
    """Here user can view only one question"""

    def get(self, questionId):
        """Get single question here."""

        try:
            val = int(questionId)
        except ValueError :
            self.response("Failed", "only numbers are allowed for questionIds")
        else:
            for msg in self.cont:
                if msg["id"] == val:
                    return self.response("question", msg)
            return self.response("Failed", "Sorry, No such question")        


class Answer(Resource, Data, GreatHelper):
    """Here user can answer a question"""

    def post(self, questionId):
        """Answer a single question at a time."""
        
        try:
            val = int(questionId)
        except ValueError:
            self.response("Failed", "only numbers are allowed for questionIds")
        else:
            for msg in self.cont:
                if msg["id"] == val and request.content_type == 'application/json':
                    info = request.get_json()
                    if info != '':
                        msg["answer"] = info
                        return self.response("Great", "Thanks for answering on platform this")
            return False    
