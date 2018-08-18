"""Helper module."""

from flask import jsonify, make_response

class GreatHelper:
    """Supports views module"""


    def response(self, message, state):
        cont = jsonify({"state": state, "message": message })
        return make_response(cont)
