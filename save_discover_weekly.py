import json
import requests

from spotify_secrets import spotify_user_id, discover_weekly_id, discover_forever_id
from refresh import Refresh

class AddSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ''
        self.discover_weekly_id = discover_weekly_id
        self.discover_forever_id = discover_forever_id
        self.headers = {}
        self.tracks = ''
        self.ids = ''
        
    def find_songs(self):
        
        print('Finding songs in Discover Weekly...')
        
        # Loop through tracks in playlist and add to list
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(discover_weekly_id)
        response = requests.get(query, headers=self.headers)
        response_json = response.json()
        
        # Create comma-seperated list of track URIs
        for i in response_json['items']:
            self.tracks += i['track']['uri'] + ','
            self.ids += i['track']['id'] +','
        self.tracks = self.tracks[:-1]
        self.ids = self.ids[:-1]
        
        return self.ids
        
    def add_songs_to_playlist(self):
        
        print('Adding songs to playlist...')
        
        # Add self.tracks to predefined playlist
        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(discover_forever_id, self.tracks)
        response = requests.post(query, headers=self.headers)
        response_json = response.json()
        
    def find_overlap(self):
        
        print('Finding overlap in Discover Weekly songs...')
        
        # Find overlapping songs between two predefined playlists
        
    def call_refresh(self):
        
        print('Refreshing token...')
        
        # Refresh token and call find_songs
        self.spotify_token = Refresh().refresh()
        self.headers = {'Content-Type':'application/json', 'Authorization':'Bearer {}'.format(self.spotify_token)}
        
        return self.headers

a = AddSongs()
a.call_refresh()
a.find_songs()
a.add_songs_to_playlist()