import jwt
import base64
import json


class _JWT():

    token = None

    def __init__(self, params):
        self.token = params

    def decode_payload(self):
        """Returns a json object of decoded payload in the jwt provided"""
        jwt_payload = self.token.split('.')[1]
        return json.loads(base64.b64decode(jwt_payload + '=' * (-len(jwt_payload) % 4)).decode('ascii'))
