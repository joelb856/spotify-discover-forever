import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import spotipy
from sklearn.cluster import KMeans
from scipy.stats import gaussian_kde
from spotipy.oauth2 import SpotifyClientCredentials

from spotify_secrets import client_id, client_secret, spotify_user_id, discover_forever_id, master_playlist_id

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=auth_manager)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def distance_from_median(df):
    median = df.median(axis=0)
    nrows = df.shape[0]

    median_matrix = np.transpose(np.vstack([median]*nrows))
    coordinates_matrix = np.transpose(df)
    distances = np.linalg.norm(median_matrix - coordinates_matrix, axis=0)

    return distances

def load_playlist(filepath, spotify_user_id, playlist_id, from_csv=True):

    if (from_csv == True):
        print('Reading in playlist CSV...')
        df = pd.read_csv(filepath)
    else:
        df = playlist_to_df(spotify_user_id, playlist_id)
        df.to_csv(filepath,index=False)

    return df

def playlist_to_df(spotify_user_id, playlist_id):
    
    columns = ['name','artist','acousticness','danceability','duration_ms','energy','instrumentalness','liveness','loudness','speechiness','tempo','valence']
    df = pd.DataFrame(columns=columns)
    
    results = sp.user_playlist_tracks(spotify_user_id,playlist_id)
    items = results['items']
    for items in results['items']:        

        audio_features = sp.audio_features(items['track']['uri'])[0]
        data = [[items['track']['name'], items['track']['artists'][0]['name'], audio_features['acousticness'],audio_features['danceability'],audio_features['duration_ms'],audio_features['energy'],audio_features['instrumentalness'],audio_features['liveness'],audio_features['loudness'],audio_features['speechiness'],audio_features['tempo'],audio_features['valence']]]

        new_row = pd.DataFrame(data,columns=columns)
        df = pd.concat([df,new_row])
        clear_terminal()
        print('Reading in {} songs...'.format(len(df.index)))

    while results['next']:

        results = sp.next(results)
        items = results['items']
        for items in results['items']: 

            audio_features = sp.audio_features(items['track']['uri'])[0]
            data = [[items['track']['name'], items['track']['artists'][0]['name'], audio_features['acousticness'],audio_features['danceability'],audio_features['duration_ms'],audio_features['energy'],audio_features['instrumentalness'],audio_features['liveness'],audio_features['loudness'],audio_features['speechiness'],audio_features['tempo'],audio_features['valence']]]

            new_row = pd.DataFrame(data,columns=columns)
            df = pd.concat([df,new_row])
            clear_terminal()
            print('Reading in {} songs...'.format(len(df.index)))
        
    return df.reset_index(drop=True)

def projected_scatter(df):

    print('Making cool plots...')

    distances = distance_from_median(df)
    df.iloc[distances.argsort()]

    n_dimensions = len(df.columns) - 1
    fig, ax = plt.subplots(n_dimensions, n_dimensions, figsize=(10,10))

    for i in range(n_dimensions):

        y_name = df.columns[i + 1]
        for j in range(n_dimensions):

            if (j <= i):

                x_name = df.columns[j]
                x = df[x_name]
                y = df[y_name]
                # xy = np.vstack([x,y])
                # z = gaussian_kde(xy)(xy)
                # idx = z.argsort()
                # x, y, z = x[idx], y[idx], z[idx]

                ax[i,j].scatter(x, y, s=3, c=distances, cmap='viridis_r')

                ax[i,j].set_xticks([])
                ax[i,j].set_yticks([])

                if (i == n_dimensions - 1):
                    ax[i,j].set_xlabel(x_name)
                if (j == 0):
                    ax[i,j].set_ylabel(y_name)
        
            else:
                ax[i,j].axis('off')
    plt.subplots_adjust(hspace=.0)
    plt.subplots_adjust(wspace=.0)
    plt.show()

df = load_playlist('all_my_songs.csv',spotify_user_id,master_playlist_id,from_csv=True)
df_features = df.drop(['name','artist','duration_ms','tempo','loudness'], axis=1)
projected_scatter(df_features)