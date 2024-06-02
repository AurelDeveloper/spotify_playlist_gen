import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import Counter

load_dotenv()

# API Auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope="playlist-modify-public user-library-read"
))

keywords = ["uk drill", "uk rap", "uk drill rap", "uk drill drip"]
all_playlists = []

for keyword in keywords:
    result = sp.search(q=f'playlist:{keyword}', type='playlist', limit=50)
    all_playlists.extend(result['playlists']['items'])

unique_playlists = {p['id']: p for p in all_playlists}.values()

tracks = []
for playlist in unique_playlists:
    response = sp.playlist_tracks(playlist['id'])
    while response:
        tracks.extend([track['track'] for track in response['items'] if track['track']])
        response = sp.next(response) if response['next'] else None

popular_tracks = [track for track in tracks if track['popularity'] > 50]
less_popular_tracks = [track for track in tracks if track['popularity'] <= 50]

user_id = sp.current_user()['id']
new_playlist = sp.user_playlist_create(user_id, 'Balanced Multi-Keyword Tracks', public=True)

playlist_tracks = []
for p_track, lp_track in zip(popular_tracks, less_popular_tracks):
    playlist_tracks.extend([p_track['id'], lp_track['id']])
    if len(playlist_tracks) >= 50:
        break

sp.playlist_add_items(new_playlist['id'], playlist_tracks[:50])