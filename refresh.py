import requests
import base64
import json

from spotify_secrets import client_id, client_secret, refresh_token

class Refresh:
    
    def __init__(self):
        
        self.client_id = client_id
        self.refresh_token = refresh_token
        
    def refresh(self):
        
        auth_str = bytes('{}:{}'.format(client_id, client_secret), 'utf-8')
        
        query = 'https://accounts.spotify.com/api/token'
        b64_auth_str = base64.b64encode(auth_str).decode('utf-8')
        request_body = {'grant_type': 'refresh_token', 'refresh_token': refresh_token}
        headers = {'Authorization':'Basic '+b64_auth_str, 'Content-Type':'application/x-www-form-urlencoded'}
        response = requests.post(query, data=request_body, headers=headers)
        response_json = response.json()

        return response_json['access_token']