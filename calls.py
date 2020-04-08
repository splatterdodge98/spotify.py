import requests
import objects

def getAlbum(refresh_token, client_id, client_secret, id):
    new_access_token = requests.post('https://accounts.spotify.com/api/token', data = {'grant_type':'refresh_token', 'refresh_token':refresh_token, 'client_id':client_id, 'client_secret':client_secret})
    access_token = new_access_token.json()['access_token']
    album_temp = requests.get("https://api.spotify.com/v1/albums/%s" % id, headers = {'Authorization': 'Bearer ' + access_token})
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

    return_obj = objects.Album(album["album_type"], list_of_artists, album['external_ids'], album['external_urls'], album['genres'], album['id'], list_of_images, album['name'], album['release_date'], list_of_tracks, album['uri'])
    return return_obj

##############
# Artist API #
##############

def getArtist(refresh_token, client_id, client_secret, artist_id):
    new_access_token = requests.post('https://accounts.spotify.com/api/token',
                                     data={'grant_type': 'refresh_token', 'refresh_token': refresh_token,
                                           'client_id': client_id, 'client_secret': client_secret})
    access_token = new_access_token.json()['access_token']
    artist_temp = requests.get("https://api.spotify.com/v1/artists/%s" % artist_id,
                              headers={'Authorization': 'Bearer ' + access_token})
    artist = artist_temp.json()
    list_of_images = []
    for images in artist["images"]:
        list_of_images.append(images["url"])
    return_obj = objects.Artist(artist["external_urls"], artist["followers"]["total"], artist["genres"], artist["href"], artist["id"], list_of_images, artist["name"], artist["popularity"], artist["type"], artist["uri"])
    return return_obj

def getManyArtists(refresh_token, client_id, client_secret, list_of_ids):
    new_access_token = requests.post('https://accounts.spotify.com/api/token',
                                     data={'grant_type': 'refresh_token', 'refresh_token': refresh_token,
                                           'client_id': client_id, 'client_secret': client_secret})
    access_token = new_access_token.json()['access_token']
    starting_list = requests.get("https://api.spotify.com/v1/%s" % list_of_ids,
                              headers={'Authorization': 'Bearer ' + access_token})
    real_list = starting_list.json()
    actual_ids = list_of_ids.split(',', 49)
    id_loc = 0
    returned_list = {}
    for artist in real_list["artists"]:
        name = artist["name"]
        returned_list[name] = actual_ids[id_loc]
        id_loc += 1
    return returned_list
