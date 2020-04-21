import requests
import objects

###########################
# Getting an Access Token # Note: You break this, and you break every other last function here.
########################### Plz Do Not Touch

def getAccessToken(refresh_token, client_id, client_secret):
    new_access_token = requests.post('https://accounts.spotify.com/api/token',
                                     data={'grant_type': 'refresh_token', 'refresh_token': refresh_token,
                                           'client_id': client_id, 'client_secret': client_secret})
    access_token = new_access_token.json()['access_token']
    return access_token

##############
# Album  API #
##############

def getAlbum(refresh_token, client_id, client_secret, id):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    album_temp = requests.get("https://api.spotify.com/v1/albums/%s" % id,
                              headers = {'Authorization': 'Bearer ' + access_token})
    album = album_temp.json()
    list_of_artists = {}
    list_of_tracks = {}
    list_of_images = []
    for artist in album["artists"]:
        list_of_artists[artist["name"]]: artist['id']
    for tracks in album['tracks']['items']:
        list_of_tracks[tracks['name']]: tracks['id']
    for images in album['images']:
        list_of_images.append(images['url'])
    return_obj = objects.Album(album["album_type"], list_of_artists, album['external_ids'], album['external_urls'],
                               album['genres'], album['id'], list_of_images, album['name'], album['release_date'],
                               list_of_tracks, album['uri'])
    return return_obj

##############
# Artist API #
##############

def getArtist(refresh_token, client_id, client_secret, artist_id):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    artist_temp = requests.get("https://api.spotify.com/v1/artists/%s" % artist_id,
                              headers={'Authorization': 'Bearer ' + access_token})
    artist = artist_temp.json()
    list_of_images = []
    for images in artist["images"]:
        list_of_images.append(images["url"])
    return_obj = objects.Artist(artist["external_urls"], artist["followers"]["total"], artist["genres"],
                                artist["href"], artist["id"], list_of_images, artist["name"], artist["popularity"],
                                artist["type"], artist["uri"])
    return return_obj

def getManyArtists(refresh_token, client_id, client_secret, list_of_ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_list = requests.get("https://api.spotify.com/v1/artists",
                              headers={'Authorization': 'Bearer ' + access_token}, params={'ids': list_of_ids})
    real_list = starting_list.json()
    returned_list = []
    for artist in real_list["artists"]:
        list_of_images = []
        for images in artist["images"]:
            list_of_images.append(images["url"])
        return_obj = objects.Artist(artist["external_urls"], artist["followers"]["total"], artist["genres"],
                                    artist["href"], artist["id"], list_of_images, artist["name"], artist["popularity"],
                                    artist["type"], artist["uri"])
        returned_list.append(return_obj)
    return returned_list

def getArtistsAlbums(refresh_token, client_id, client_secret, artist_id):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_list = requests.get("https://api.spotify.com/v1/artists/%s/albums" % artist_id,
                                 headers={'Authorization': 'Bearer ' + access_token})
    real_list = starting_list.json()
    album_list = []
    for album in real_list['items']:
        artist_dict = {}
        list_of_images = []
        for artist in album['artists']:
            artist_dict[artist['name']]: artist['id']
        for image in album['images']:
            list_of_images.append(image['url'])
        temp_album = objects.Album(album['album_type'], artist_dict, {}, album['external_urls'], [], album['id'],
                                   list_of_images, album['name'], album['release_date'], {}, album['uri'])
        album_list.append(temp_album)
    return album_list

def getArtistsTopTracks(refresh_token, client_id, client_secret, artist_id, country):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_list = requests.get("https://api.spotify.com/v1/artists/%s/top-tracks" % artist_id,
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'market': country})
    real_list = starting_list.json()
    track_list = []
    for track in real_list['tracks']:
        list_of_artists = []
        for artist in track['artists']:
            list_of_artists.append(artist['name'])
        temp_markets = []
        temp_track = objects.Track(track['album']['id'], list_of_artists, temp_markets,
                                   track['disc_number'], track['duration_ms'], track['explicit'], track['external_ids'],
                                   track['external_urls'], track['href'], track['id'], track['name'],
                                   track['popularity'], track['preview_url'], track['track_number'], track['type'],
                                   track['uri'], None)
        track_list.append(temp_track)
    return track_list

def getArtistsSimilarArtists(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    return 0

##############
# Track  API #
##############

def getManyTracks(refresh_token, client_id, client_secret, list_of_ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tracksTempCall = requests.get('https://api.spotify.com/v1/tracks/',
                              headers={'Authorization': 'Bearer ' + access_token},
                              params={'ids': list_of_ids})
    tracksTemp = tracksTempCall.json()
    tracks = []
    for i in tracksTemp['tracks']:
        all_artists = []
        available_markets = i['available_markets']
        for j in i['artists']:
            all_artists.append([j['name']])
        tracks.append(objects.Track(i['album']['id'], all_artists, available_markets, i['disc_number'],
                                    i['duration_ms'], i['explicit'], i['external_ids'], i['external_urls'], i['href'],
                                    i['id'], i['name'], i['popularity'], i['preview_url'], i['track_number'],
                                    i['type'], i['uri'], i['is_local']))
    return tracks

def getAudioAnalysisForTrack(refresh_token, client_id, client_secret, trackId):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/audio-analysis/%s' % trackId,
                            headers={'Authorization': 'Bearer ' + access_token})
    return tempCall.json()

def getAudioFeaturesForTrack(refresh_token, client_id, client_secret, trackId):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/audio-features/%s' % trackId,
                            headers={'Authorization': 'Bearer ' + access_token})
    AudioFeaturestemp = tempCall.json()
    return objects.AudioFeatureObject(AudioFeaturestemp['acousticness'], AudioFeaturestemp['analysis_url'],
                                      AudioFeaturestemp['danceability'], AudioFeaturestemp['duration_ms'],
                                      AudioFeaturestemp['energy'], AudioFeaturestemp['id'],
                                      AudioFeaturestemp['instrumentalness'], AudioFeaturestemp['key'],
                                      AudioFeaturestemp['liveness'], AudioFeaturestemp['loudness'],
                                      AudioFeaturestemp['mode'], AudioFeaturestemp['speechiness'],
                                      AudioFeaturestemp['tempo'], AudioFeaturestemp['time_signature'],
                                      AudioFeaturestemp['track_href'], AudioFeaturestemp['type'],
                                      AudioFeaturestemp['uri'], AudioFeaturestemp['valence'])

def getTrack(refresh_token, client_id, client_secret, trackId):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/tracks/%s' % trackId,
                            headers={'Authorization': 'Bearer ' + access_token})
    trackTemp = tempCall.json()
    available_markets = trackTemp['available_markets']
    all_artists = []
    for i in trackTemp['artists']:
        all_artists.append([i['name']])
    return objects.Track(trackTemp['album']['id'], all_artists, available_markets, trackTemp['disc_number'],
                         trackTemp['duration_ms'], trackTemp['explicit'], trackTemp['external_ids'],
                         trackTemp['external_urls'], trackTemp['href'], trackTemp['id'], trackTemp['name'],
                         trackTemp['popularity'], trackTemp['preview_url'], trackTemp['track_number'],
                         trackTemp['type'], trackTemp['uri'], trackTemp['is_local'])
