"""This file holds the setup for the test file"""

import unittest

import json

from app import app

from app.config  import app_config

class TestCases(unittest.TestCase):
    """This is the main test class. """


    def setUp(self):
        """Its the first method to be called"""
        self.info = {"msg": " How do i connect to heroku. "}

        self.client = app.test_client(self)

        # app.config.from_object(app_config["testing"])

        # return app


    def test_question_content(self):
        """check effect when other than json is sent."""

        result = self.client.post('/api/v1/questions', data = "", content_type = 'application/json')
        
        self.assertEqual(result.status_code, 400)


    def test_post_question(self):
        """check effect when json is sent."""

        result = self.client.post('/api/v1/questions', data = json.dumps(self.info), content_type = 'application/json')
        
        self.assertEqual(result.status_code, 200)


    def test_view_all_questions(self):
        """test viewing all questions."""

        result = self.client.get('/api/v1/questions', content_type = 'application/json')
        
        self.assertEqual(result.status_code, 200)  


    def test_view_single_questions_one(self):
        """test viewing single question with fake id."""
        questionId = "gdfr"

        result = self.client.get('/api/v1/questions/{}'.format(questionId), content_type = 'application/json')
        
        self.assertEqual(result.status_code, 200)      

    
    def test_view_single_questions_two(self):
        """test viewing single question with right id."""
        questionId = 100

        result = self.client.get('/api/v1/questions/{}'.format(questionId), content_type = 'application/json')
        
        self.assertEqual(result.status_code, 200)    