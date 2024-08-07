### Spotify Playlist Script

This Python script uses the Spotipy library to interact with the Spotify Web API. It searches Spotify for playlists containing specific keywords, collects tracks from these playlists, and creates a new playlist featuring a balanced mix of popular and less popular tracks.

## Prerequisites
- Python 3.x
- Spotipy library
- A Spotify Developer Account

## Installation
1. Install the required packages:
   ```bash
   pip install spotipy python-dotenv
   ```
2. Create a `.env` file in the same directory as your script with the following content:
   ```bash
   SPOTIPY_CLIENT_ID='YourSpotifyClientId'
   SPOTIPY_CLIENT_SECRET='YourSpotifyClientSecret'
   SPOTIPY_REDIRECT_URI='http://localhost:3000'
   ```
   Replace `YourSpotifyClientId`, `YourSpotifyClientSecret`, and `YourRedirectUri` with your own Spotify API credentials.

## Authentication
The script uses OAuth 2.0 authentication to make secure requests to the Spotify API. The credentials are loaded from the `.env` file and used to create a `SpotifyOAuth` object, which is necessary for authentication.

## How the Script Works

1. **Loading Environment Variables**:
   - `load_dotenv()`: Loads the environment variables from the `.env` file.

2. **Initializing the Spotipy Client Instance**:
   - `SpotifyOAuth`: Authenticates the user and enables API access.
   - `spotipy.Spotify`: Creates a Spotipy client instance with the OAuth object.

3. **Searching for Playlists**:
   - For each keyword in the `keywords` list, the `search()` method is used to find playlists containing the keyword. The results are collected in `all_playlists`.

4. **Removing Duplicates**:
   - Duplicates are removed by using a dictionary that uses playlist IDs as keys. Only unique playlists are retained.

5. **Collecting Tracks**:
   - Tracks are collected from each unique playlist. Pagination is used to ensure all tracks are retrieved.

6. **Separating Tracks by Popularity**:
   - Tracks are divided into `popular_tracks` and `less_popular_tracks` based on their popularity.

7. **Creating a New Playlist**:
   - A new playlist is created in the user's account.

8. **Adding Tracks to the Playlist**:
   - Tracks from both `popular_tracks` and `less_popular_tracks` are alternately added to the new playlist to maintain a balance. The process stops once 50 tracks have been added or there are no more tracks to add.

This script automates the process of creating a balanced Spotify playlist based on predefined keywords by searching for public playlists, collecting tracks, and organizing them based on their popularity in a new playlist.
