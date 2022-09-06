import hashlib
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv



load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class AuthRepositories:
    auth_url = None
    api_key = os.getenv('API_KEY')
    secret_key = os.getenv('SECRET_KEY')

    @classmethod
    def auth(cls, uuid):
        url = "http://www.last.fm/api/auth/?api_key="
        cb = f"&cb=http://127.0.0.1:8000/{uuid}/"
        cls.auth_url = url+cls.api_key+cb

    @classmethod
    def session(cls, token):
        hash = cls.hash(token)
        response = requests.get(f"http://ws.audioscrobbler.com/2.0/?method=auth.getSession&api_key={cls.api_key}&token={token}&api_sig={hash}&format=json")
        data = json.loads(response.text)
        return data['session']

    @classmethod
    def hash(cls, token):
        str = f"api_key{cls.api_key}methodauth.getSessiontoken{token}{cls.secret_key}"
        return hashlib.md5(str.encode('utf-8')).hexdigest()

    @classmethod
    def request_trek(cls, username):
        response = requests.get(
            f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&limit=1&api_key={cls.api_key}&format=json")
        data = json.loads(response.text)
        return data['recenttracks']['track'][0]
