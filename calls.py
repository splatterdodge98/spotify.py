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

################
# Library  API #
################

def saveTracksforUser(refresh_token, client_id, client_secret, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.put("https://api.spotify.com/v1/me/tracks",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'ids': ids})
    return starting_info

def removeUsersSavedTracks(refresh_token, client_id, client_secret, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.delete("https://api.spotify.com/v1/me/tracks",
                                    headers={'Authorization': 'Bearer ' + access_token},
                                    params={'ids': ids})
    return starting_info

def checkUsersSavedTracks(refresh_token, client_id, client_secret, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/me/tracks/contains",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'ids': ids})
    info = starting_info.json()
    return info

def getUsersSavedTracks(refresh_token, client_id, client_secret, num=20, start=0):
    if num > 50:
        num = 50
    if num < 1:
        num = 1
    if start < 0:
        start = 0
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/me/tracks",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'limit': num, 'offset': start})
    info = starting_info.json()
    list_of_tracks = []
    for track in info['items']:
        list_of_artists = {}
        for artist in track['track']['artists']:
            list_of_artists[artist['name']]: artist['id']
        list_of_tracks.append(objects.SavedTrack(track['track']['album']['id'], list_of_artists,
                                                 track['track']['available_markets'], track['track']['disc_number'],
                                                 track['track']['duration_ms'], track['track']['explicit'],
                                                 track['track']['external_ids'], track['track']['external_urls'],
                                                 track['track']['href'], track['track']['id'], None, None, None,
                                                 track['track']['name'], track['track']['popularity'],
                                                 track['track']['preview_url'], track['track']['track_number'],
                                                 track['track']['type'], track['track']['uri'], None,
                                                 track['added_at']))
    paging_obj = objects.PagingObject(info['href'], list_of_tracks, info['limit'], info['next'], info['offset'],
                                      info['previous'], info['total'])
    return paging_obj

def saveAlbumsforUser(refresh_token, client_id, client_secret, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.put("https://api.spotify.com/v1/me/albums",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'ids': ids})
    return starting_info

def removeAlbumsforUser(refresh_token, client_id, client_secret, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.delete("https://api.spotify.com/v1/me/albums",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'ids': ids})
    return starting_info

def checkUsersSavedAlbums(refresh_token, client_id, client_secret, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/me/albums/contains",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'ids': ids})
    info = starting_info.json()
    return info

def getUsersSavedAlbums(refresh_token, client_id, client_secret, num=20, start=0):
    if num > 50:
        num = 50
    if num < 1:
        num = 1
    if start < 0:
        start = 0
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/me/albums",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'limit': num, 'offset': start})
    info = starting_info.json()
    list_of_albums = []
    for album in info['items']:
        list_of_artists = {}
        list_of_images = []
        list_of_tracks = []
        for artist in album['album']['artists']:
            list_of_artists[artist['name']]: artist['id']
        for image in album['album']['images']:
            list_of_images.append(image['url'])
        for track in album['album']['tracks']['items']:
            track_list_of_artists = {}
            for artist in track['artists']:
                track_list_of_artists[artist['name']]: artist['id']
            list_of_tracks.append(objects.Track(album['album']['id'], track_list_of_artists, track['available_markets'],
                                                track['disc_number'], track['duration_ms'], track['explicit'], None,
                                                track['external_urls'], track['href'], track['id'], track['name'],
                                                None, track['preview_url'], track['track_number'], track['type'],
                                                track['uri'], None))
        album_paging_object = objects.PagingObject(album['album']['tracks']['href'], list_of_tracks,
                                                   album['album']['tracks']['limit'], album['album']['tracks']['next'],
                                                   album['album']['tracks']['offset'],
                                                   album['album']['tracks']['previous'],
                                                   album['album']['tracks']['total'])
        list_of_albums.append(objects.SavedAlbum(album['album']['album_type'], list_of_artists,
                                                 album['album']['external_ids'], album['album']['external_urls'],
                                                 album['album']['genres'], album['album']['id'], list_of_images,
                                                 album['album']['name'], album['album']['release_date'],
                                                 album_paging_object, album['added_at'], album['album']['uri']))
    paging_obj = objects.PagingObject(info['href'], list_of_albums, info['limit'], info['next'], info['offset'],
                                      info['previous'], info['total'])
    return paging_obj

# IGNORE THE SHOWS FUNCTIONS FOR NOW
def saveShowsforUser(refresh_token, client_id, client_secret): # IGNORE FOR NOW
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("",
                                 headers={'Authorization': 'Bearer ' + access_token})
    info = starting_info.json()
    return 0

def removeUsersSavedShows(refresh_token, client_id, client_secret): # IGNORE FOR NOW
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("",
                                 headers={'Authorization': 'Bearer ' + access_token})
    info = starting_info.json()
    return 0

def checkUsersSavedShows(refresh_token, client_id, client_secret): # IGNORE FOR NOW
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("",
                                 headers={'Authorization': 'Bearer ' + access_token})
    info = starting_info.json()
    return 0

def getUsersSavedShows(refresh_token, client_id, client_secret): # IGNORE FOR NOW
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("",
                                 headers={'Authorization': 'Bearer ' + access_token})
    info = starting_info.json()
    return 0


##############
# Album  API #
##############

def getAnAlbum(refresh_token, client_id, client_secret, albumId):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    album_temp = requests.get("https://api.spotify.com/v1/albums/%s" % albumId,
                              headers={'Authorization': 'Bearer ' + access_token})
    album = album_temp.json()
    list_of_artists = {}
    holdingTracks = []
    list_of_images = []
    for artist in album["artists"]:
        list_of_artists[artist["name"]] = artist['id']
    for i in album['tracks']['items']:
        holdingArtists = {}
        for j in i['artists']:
            holdingArtists[j['name']] = j['id']
        holdingTracks.append(
            objects.Track(i['id'], holdingArtists, i['available_markets'], i['disc_number'], i['duration_ms'],
                          i['explicit'], None, i['external_urls'], i['href'], i['id'], i['name'], None,
                          i['preview_url'],
                          i['track_number'], i['type'], i['uri'], None))
    list_of_tracks = objects.PagingObject(album['tracks']['href'], holdingTracks, album['tracks']['limit'],
                                          album['tracks']['next'], album['tracks']['offset'],
                                          album['tracks']['previous'], album['tracks']['total'])
    for images in album['images']:
        list_of_images.append(images['url'])
    return_obj = objects.Album(album["album_type"], list_of_artists, album['external_ids'], album['external_urls'],
                               album['genres'], album['id'], list_of_images, album['name'], album['release_date'],
                               list_of_tracks, album['uri'])
    return return_obj


def getMultipleAlbums(refresh_token, client_id, client_secret, albumIds):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/albums',
                            headers={'Authorization': 'Bearer ' + access_token},
                            params={'ids': albumIds})
    tempAlbums = tempCall.json()
    albumsToReturn = []
    for i in tempAlbums['albums']:
        list_of_artists = {}
        holdingTracks = []
        list_of_images = []
        for artist in i["artists"]:
            list_of_artists[artist["name"]] = artist['id']
        for j in i['tracks']['items']:
            holdingArtists = {}
            for k in j['artists']:
                holdingArtists[k['name']] = k['id']
            holdingTracks.append(
                objects.Track(j['id'], holdingArtists, j['available_markets'], j['disc_number'], j['duration_ms'],
                              j['explicit'], None, j['external_urls'], j['href'], j['id'], j['name'], None,
                              j['preview_url'],
                              j['track_number'], j['type'], j['uri'], None))
        list_of_tracks = objects.PagingObject(i['tracks']['href'], holdingTracks, i['tracks']['limit'],
                                              i['tracks']['next'], i['tracks']['offset'],
                                              i['tracks']['previous'], i['tracks']['total'])
        for images in i['images']:
            list_of_images.append(images['url'])
        albumsToReturn.append(objects.Album(i["album_type"], list_of_artists, i['external_ids'], i['external_urls'],
                                            i['genres'], i['id'], list_of_images, i['name'], i['release_date'],
                                            list_of_tracks, i['uri']))
    return albumsToReturn


def getAnAlbumsTracks(refresh_token, client_id, client_secret, albumId):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/albums/%s/tracks' % albumId,
                            headers={'Authorization': 'Bearer ' + access_token})
    tempTracks = tempCall.json()
    holdingTracks = []
    for i in tempTracks['items']:
        holdingArtists = {}
        for j in i['artists']:
            holdingArtists[j['name']] = j['id']
        holdingTracks.append(
            objects.Track(i['id'], holdingArtists, i['available_markets'], i['disc_number'], i['duration_ms'],
                          i['explicit'], None, j['external_urls'], i['href'], i['id'], i['name'], None,
                          i['preview_url'],
                          i['track_number'], i['type'], i['uri'], None))
    return objects.PagingObject(tempTracks['href'], holdingTracks, tempTracks['limit'],
                                tempTracks['next'], tempTracks['offset'],
                                tempTracks['previous'], tempTracks['total'])


################
# Playlist API #
################

def removeItemsFromAPlaylist(refresh_token, client_id, client_secret, playlistID, type, listOfUris):
    toSend = []
    for i in listOfUris:
        toSend.append({'uri':i})
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.delete('https://api.spotify.com/v1/playlists/%s/tracks' % playlistID,
                               headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'},
                               data={type: toSend})
    return tempCall.json()['snapshot_id']

def addItemsToAPlaylist(refresh_token, client_id, client_secret, playlistID, listOfUris):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.post('https://api.spotify.com/v1/playlists/%s/tracks' % playlistID,
                             headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'},
                             data={'uris': listOfUris})
    return tempCall.json()['snapshot_id']

def getAPlaylistsItems(refresh_token, client_id, client_secret, playlistID, market):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/playlists/%s/tracks' % playlistID,
                            headers={'Authorization': 'Bearer ' + access_token},
                            params={'market': market})
    tempItems = tempCall.json()
    list_of_tracks = []
    for i in tempItems['items']:
        artists = {}
        for j in i['track']['artists']:
            artists[j['name']] = j['id']
        list_of_tracks.append(objects.PlaylistTrackObject(i['added_at'], i['added_by'], i['is_local'],
                                                          objects.Track(i['track']['album']['id'], artists,
                                                                        i['track']['available_markets'],
                                                                        i['track']['disc_number'],
                                                                        i['track']['duration_ms'],
                                                                        i['track']['explicit'],
                                                                        i['track']['external_ids'],
                                                                        i['track']['external_urls'],
                                                                        i['track']['href'], i['track']['id'],
                                                                        i['track']['name'], i['track']['popularity'],
                                                                        i['track']['preview_url'],
                                                                        i['track']['track_number'],
                                                                        i['track']['type'], i['track']['uri'], None
                                                                        )))
    return objects.PagingObject(tempItems['href'], list_of_tracks, tempItems['limit'], tempItems['next'],
                                tempItems['offset'], tempItems['previous'], tempItems['total'])

def createAPlaylist(refresh_token, client_id, client_secret, userID, name, **kwargs):
    optionalList = ['public', 'collaborative', 'description']
    jsonToPass = {'name': name}
    for key in kwargs:
        if key in optionalList:
            jsonToPass[key] = kwargs[key]
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.post('https://api.spotify.com/v1/users/%s/playlists' % userID,
                             headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'},
                             data=jsonToPass)
    tempPlaylist = tempCall.json()
    list_of_tracks = []
    for i in tempPlaylist['tracks']['items']:
        artists = {}
        for j in i['track']['artists']:
            artists[j['name']] = j['id']
        list_of_tracks.append(objects.PlaylistTrackObject(i['added_at'], i['added_by'], i['is_local'],
                                                          objects.Track(i['track']['album']['id'], artists,
                                                                        i['track']['available_markets'],
                                                                        i['track']['disc_number'],
                                                                        i['track']['duration_ms'],
                                                                        i['track']['explicit'],
                                                                        i['track']['external_ids'],
                                                                        i['track']['external_urls'],
                                                                        i['track']['href'], i['track']['id'],
                                                                        i['track']['name'], i['track']['popularity'],
                                                                        i['track']['preview_url'],
                                                                        i['track']['track_number'],
                                                                        i['track']['type'], i['track']['uri'], None
                                                                        )))
    list_of_images = []
    for i in tempPlaylist['images']:
        list_of_images.append(i['url'])

    return objects.PlaylistObject(tempPlaylist['collaborative'], tempPlaylist['description'],
                                  tempPlaylist['external_urls'], tempPlaylist['followers']['total'],
                                  tempPlaylist['href'], tempPlaylist['id'], list_of_images, tempPlaylist['name'],
                                  tempPlaylist['owner']['id'], tempPlaylist['public'], tempPlaylist['snapshot_id'],
                                  list_of_tracks, tempPlaylist['type'], tempPlaylist['uri'])

def getAListOfAUsersPlaylists(refresh_token, client_id, client_secret, userID):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/users/%s/playlists' % userID,
                            headers={'Authorization': 'Bearer ' + access_token})
    tempPlaylists = tempCall.json()
    listOfPlaylists = {}
    for i in tempPlaylists['items']:
        listOfPlaylists[i['name']] = i['id']
    return objects.PagingObject(tempPlaylists['href'], listOfPlaylists, tempPlaylists['limit'], tempPlaylists['next'],
                                tempPlaylists['offset'], tempPlaylists['previous'], tempPlaylists['total'])

def getAPlaylist(refresh_token, client_id, client_secret, playlistId):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/playlists/%s' % playlistId,
                            headers={'Authorization': 'Bearer ' + access_token})
    tempPlaylist = tempCall.json()
    list_of_tracks = []
    for i in tempPlaylist['tracks']['items']:
        artists = {}
        for j in i['track']['artists']:
            artists[j['name']] = j['id']
        list_of_tracks.append(objects.PlaylistTrackObject(i['added_at'], i['added_by'], i['is_local'],
                                                          objects.Track(i['track']['album']['id'], artists,
                                                                        i['track']['available_markets'],
                                                                        i['track']['disc_number'],
                                                                        i['track']['duration_ms'],
                                                                        i['track']['explicit'],
                                                                        i['track']['external_ids'],
                                                                        i['track']['external_urls'],
                                                                        i['track']['href'], i['track']['id'],
                                                                        i['track']['name'], i['track']['popularity'],
                                                                        i['track']['preview_url'],
                                                                        i['track']['track_number'],
                                                                        i['track']['type'], i['track']['uri'], None
                                                                        )))
    list_of_images = []
    for i in tempPlaylist['images']:
        list_of_images.append(i['url'])

    return objects.PlaylistObject(tempPlaylist['collaborative'], tempPlaylist['description'],
                                  tempPlaylist['external_urls'], tempPlaylist['followers']['total'],
                                  tempPlaylist['href'], tempPlaylist['id'], list_of_images, tempPlaylist['name'],
                                  tempPlaylist['owner']['id'], tempPlaylist['public'], tempPlaylist['snapshot_id'],
                                  list_of_tracks, tempPlaylist['type'], tempPlaylist['uri'])

def getAListOfAUsersPlaylists(refresh_token, client_id, client_secret, userID):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/users/%s/playlists' % userID,
                            headers={'Authorization': 'Bearer ' + access_token})
    tempList = tempCall.json()
    list_of_playlists = []
    for i in tempList['items']:
        list_of_images = []
        for j in i['images']:
            list_of_images.append(j['url'])
        list_of_playlists.append(objects.PlaylistObject(i['collaborative'], None,
                                  i['external_urls'], None,
                                  i['href'], i['id'], list_of_images, i['name'],
                                  i['owner']['id'], i['public'], i['snapshot_id'],
                                  i['tracks']['total'], i['type'], i['uri']))
    return list_of_playlists

def getAPlaylistCoverImage(refresh_token, client_id, client_secret, playlistID):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/playlists/%s/images' % playlistID,
                            headers={'Authorization': 'Bearer ' + access_token})
    list_of_images =[]
    for i in tempCall.json():
        list_of_images.append(i['url'])

    return list_of_images

def changeAPlaylistsDetails(refresh_token, client_id, client_secret, playlistID, **kwargs):
    optionalList = ['name', 'public', 'collaborative', 'description']
    jsonToPass = {}
    for key in kwargs:
        if key in optionalList:
            jsonToPass[key] = kwargs[key]
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.put('https://api.spotify.com/v1/playlists/%s' % playlistID,
                            headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'},
                            data=jsonToPass)
    return tempCall

def reorderAPlaylistsItems(refresh_token, client_id, client_secret, playlistID, range_start, insert_before, **kwargs):
    optionalList = ['range_length', 'snapshot_id']
    jsonToPass = {'range_start':range_start, 'insert_before':insert_before}
    for key in kwargs:
        if key in optionalList:
            jsonToPass[key] = kwargs[key]
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.put('https://api.spotify.com/v1/playlists/%s/tracks' % playlistID,
                            headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'},
                            data=jsonToPass)
    return tempCall.json()['snapshot_id']

def replaceAPlaylistsItems(refresh_token, client_id, client_secret, uris, playlistId):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.put('https://api.spotify.com/v1/playlists/%s/tracks' % playlistId,
                            headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'},
                            data={'uris': uris})
    return tempCall

def uploadACustomPlaylistCoverImage(refresh_token, client_id, client_secret, playlistID, imageB64):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.put('https://api.spotify.com/v1/playlists/%s/images' % playlistID,
                            headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'image/jpeg'},
                            data= imageB64)
    return tempCall

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
        list_of_artists = {}
        for artist in track['artists']:
            list_of_artists[artist['name']]: artist['id']
        temp_track = objects.Track(track['album']['id'], list_of_artists, None,
                                   track['disc_number'], track['duration_ms'], track['explicit'], track['external_ids'],
                                   track['external_urls'], track['href'], track['id'], track['name'],
                                   track['popularity'], track['preview_url'], track['track_number'], track['type'],
                                   track['uri'], track['is_local'])
        track_list.append(temp_track)
    return track_list


def getArtistRelatedArtists(refresh_token, client_id, client_secret, artist_id):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_list = requests.get("https://api.spotify.com/v1/artists/%s/related-artists" % artist_id,
                                 headers={'Authorization': 'Bearer ' + access_token})
    real_list = starting_list.json()
    list_of_artists = []
    for artist in real_list["artists"]:
        list_of_images = []
        for images in artist["images"]:
            list_of_images.append(images["url"])
        temp_artist = objects.Artist(artist["external_urls"], artist["followers"]["total"], artist["genres"],
                                     artist["href"], artist["id"], list_of_images, artist["name"], artist["popularity"],
                                     artist["type"], artist["uri"])
        list_of_artists.append(temp_artist)
    return list_of_artists


####################
# User Profile API #
####################

def getOtherUsersProfile(refresh_token, client_id, client_secret, user_id):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/users/%s" % user_id,
                                 headers={'Authorization': 'Bearer ' + access_token})
    real_info = starting_info.json()
    list_of_images = []
    for image in real_info['images']:
        list_of_images.append(image['url'])
    user_info = objects.PublicUserObject(real_info['display_name'], real_info['external_urls'],
                                         real_info['followers']['total'], real_info['href'], real_info['id'],
                                         list_of_images, real_info['type'], real_info['uri'])
    return user_info


def getCurrentUsersProfile(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/me",
                                 headers={'Authorization': 'Bearer ' + access_token})
    real_info = starting_info.json()
    list_of_images = []
    for image in real_info['images']:
        list_of_images.append(image['url'])
    user_info = objects.PrivateUserObject(real_info['country'], real_info['display_name'], real_info['email'],
                                          real_info['external_urls'], real_info['followers']['total'],
                                          real_info['href'], real_info['id'], list_of_images, real_info['product'],
                                          real_info['type'], real_info['uri'])
    return user_info


###############
# Browse  API #
###############

def getManyCategories(refresh_token, client_id, client_secret, num=20, start=0):
    if num > 50:
        num = 50
    if num < 1:
        num = 1
    if start < 0:
        start = 0
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/browse/categories",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'limit': num, 'offset': start})
    info = starting_info.json()
    category_list = []
    for category in info['categories']['items']:
        icon_list = []
        for icon in category['icons']:
            icon_list.append(icon['url'])
        temp_category = objects.Category(category['href'], icon_list, category['id'], category['name'])
        category_list.append(temp_category)
    return category_list


def getACategory(refresh_token, client_id, client_secret, category_id):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/browse/categories/%s" % category_id,
                                 headers={'Authorization': 'Bearer ' + access_token})
    info = starting_info.json()
    icon_list = []
    for icon in info['icons']:
        icon_list.append(icon['url'])
    category = objects.Category(info['href'], icon_list, info['id'], info['name'])
    return category


def getACategorysPlaylists(refresh_token, client_id, client_secret, category_id, num=20, start=0):
    if num > 50:
        num = 50
    if num < 1:
        num = 1
    if start < 0:
        start = 0
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/browse/categories/%s/playlists" % category_id,
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'limit': num, 'offset': start})
    info = starting_info.json()
    list_of_playlists = []
    for playlist in info['playlists']['items']:
        list_of_images = []
        for image in playlist['images']:
            list_of_images.append(image['url'])
        temp_playlist = objects.PlaylistObject(playlist['collaborative'], playlist['external_urls'], playlist['href'],
                                               playlist['id'], list_of_images, playlist['name'],
                                               playlist['owner']['display_name'], playlist['public'],
                                               playlist['snapshot_id'], playlist['tracks'], playlist['type'],
                                               playlist['uri'])
        list_of_playlists.append(temp_playlist)
    return list_of_playlists


def getRecommendations(refresh_token, client_id, client_secret, input_artists, input_genres, input_tracks, num=20):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/recommendations",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'seed_artists': input_artists, 'seed_genres': input_genres,
                                         'seed_tracks': input_tracks, 'limit': num})
    info = starting_info.json()
    track_list = []
    seed_list = []
    for track in info['tracks']:
        artists = []
        for artist in track['artists']:
            artists.append([artist['name']])
        temp_track = objects.Track(track['album']['id'], artists, None, track['disc_number'], track['duration_ms'],
                                   track['explicit'], track['external_ids'], track['external_urls'], track['href'],
                                   track['id'], track['name'], track['popularity'], track['preview_url'],
                                   track['track_number'], track['type'], track['uri'], track['is_local'])
        track_list.append(temp_track)
    for seed in info['seeds']:
        temp_seed = objects.RecommendationSeedObject(seed['initialPoolSize'], seed['afterFilteringSize'],
                                                     seed['afterRelinkingSize'], seed['href'], seed['id'], seed['type'])
        seed_list.append(temp_seed)
    recommends_response = objects.RecommendationsResponseObject(seed_list, track_list)
    return recommends_response


def getRecommendationGenres(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/recommendations/available-genre-seeds",
                                 headers={'Authorization': 'Bearer ' + access_token})
    info = starting_info.json()
    return_list = info['genres']
    return return_list


def getAllNewReleases(refresh_token, client_id, client_secret, num=20, start=0):
    if num > 50:
        num = 50
    if num < 1:
        num = 1
    if start < 0:
        start = 0
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/browse/new-releases",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'limit': num, 'offset': start})
    info = starting_info.json()
    album_list = []
    for album in info['albums']['items']:
        artist_dict = {}
        list_of_images = []
        for artist in album['artists']:
            artist_dict[artist['name']]: artist['id']
        for image in album['images']:
            list_of_images.append(image['url'])
        album_list.append(objects.Album(album['album_type'], artist_dict, None, album['external_urls'], None,
                                        album['id'], list_of_images, album['name'], album['release_date'], None,
                                        album['uri']))
    paging_obj = objects.PagingObject(info['albums']['href'], album_list, info['albums']['limit'],
                                      info['albums']['next'], info['albums']['offset'], info['albums']['previous'],
                                      info['albums']['total'])
    return paging_obj


def getAllFeaturedPlaylists(refresh_token, client_id, client_secret, num=20, start=0):
    if num > 50:
        num = 50
    if num < 1:
        num = 1
    if start < 0:
        start = 0
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/browse/featured-playlists",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'limit': num, 'offset': start})
    info = starting_info.json()
    list_of_playlists = []
    for playlist in info['playlists']['items']:
        list_of_images = []
        for image in playlist['images']:
            list_of_images.append(image['url'])
        list_of_playlists.append(objects.PlaylistObject(playlist['collaborative'], playlist['external_urls'],
                                                        playlist['href'], playlist['id'], list_of_images,
                                                        playlist['name'], playlist['owner']['display_name'],
                                                        playlist['public'], playlist['snapshot_id'],
                                                        playlist['tracks'], playlist['type'], playlist['uri']))
    paging_obj = objects.PagingObject(info['playlists']['href'], list_of_playlists, info['playlists']['limit'],
                                      info['playlists']['next'], info['playlists']['offset'],
                                      info['playlists']['previous'], info['playlists']['total'])
    return paging_obj


###############
# Follow  API #
###############

def getFollowingState(refresh_token, client_id, client_secret, type, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/me/following/contains",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'type': type, 'ids': ids})
    info = starting_info.json()
    return info


def checkIfUsersFollowAPlaylist(refresh_token, client_id, client_secret, playlist_id, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/playlists/%s/followers/contains" % playlist_id,
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'ids': ids})
    info = starting_info.json()
    return info


def followAnArtistOrUser(refresh_token, client_id, client_secret, type, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.put("https://api.spotify.com/v1/me/following",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'type': type, 'ids': ids})
    return starting_info


def followAPlaylist(refresh_token, client_id, client_secret, playlist_id):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.put("https://api.spotify.com/v1/playlists/%s/followers" % playlist_id,
                                 headers={'Authorization': 'Bearer ' + access_token})
    return starting_info


def getUsersFollowedArtists(refresh_token, client_id, client_secret, type, num=20):
    if num > 50:
        num = 50
    if num < 1:
        num = 1
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/me/following",
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'type': type, 'limit': num})
    info = starting_info.json()
    list_of_artists = []
    for artist in info['artists']['items']:
        list_of_images = []
        for images in artist["images"]:
            list_of_images.append(images["url"])
        list_of_artists.append(objects.Artist(artist["external_urls"], artist["followers"]["total"], artist["genres"],
                                              artist["href"], artist["id"], list_of_images, artist["name"],
                                              artist["popularity"], artist["type"], artist["uri"]))
    cursor_obj = objects.CursorBasedPagingObject(info['artists']['href'], list_of_artists, info['artists']['next'],
                                                 info['artists']['cursors'], info['artists']['total'])
    return cursor_obj


def unfollowArtistsOrUsers(refresh_token, client_id, client_secret, type, ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.delete("https://api.spotify.com/v1/me/following",
                                    headers={'Authorization': 'Bearer ' + access_token},
                                    params={'type': type, 'ids': ids})
    return starting_info


def unfollowAPlaylist(refresh_token, client_id, client_secret, playlist_id):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.delete("https://api.spotify.com/v1/playlists/%s/followers" % playlist_id,
                                 headers={'Authorization': 'Bearer ' + access_token})
    return starting_info


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
        all_artists = {}
        available_markets = i['available_markets']
        for j in i['artists']:
            all_artists[j['name']]: j['id']
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
    all_artists = {}
    for i in trackTemp['artists']:
        all_artists[i['name']]: i['id']
    return objects.Track(trackTemp['album']['id'], all_artists, available_markets, trackTemp['disc_number'],
                         trackTemp['duration_ms'], trackTemp['explicit'], trackTemp['external_ids'],
                         trackTemp['external_urls'], trackTemp['href'], trackTemp['id'], trackTemp['name'],
                         trackTemp['popularity'], trackTemp['preview_url'], trackTemp['track_number'],
                         trackTemp['type'], trackTemp['uri'], trackTemp['is_local'])


def getAudioFeaturesForSeveralTracks(refresh_token, client_id, client_secret, list_of_ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/audio-features',
                            headers={'Authorization': 'Bearer ' + access_token},
                            params={'ids': list_of_ids})
    tempAudioFeature = tempCall.json()
    AudioFeaturelist = []
    for i in tempAudioFeature['audio_features']:
        if i is not None:
            AudioFeaturelist.append(
                objects.AudioFeatureObject(i['acousticness'], i['analysis_url'], i['danceability'], i['duration_ms'],
                                           i['energy'], i['id'], i['instrumentalness'], i['key'], i['liveness'],
                                           i['loudness'],
                                           i['mode'], i['speechiness'], i['tempo'], i['time_signature'],
                                           i['track_href'], i['type'], i['uri'], i['valence']))
    return AudioFeaturelist


##############
# Search API #
##############

def searchForAnItem(refresh_token, client_id, client_secret, q, type):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    tempCall = requests.get('https://api.spotify.com/v1/search',
                            headers={'Authorization': 'Bearer ' + access_token},
                            params={'q': q, 'type': type})
    searchTemp = tempCall.json()
    if type == 'track':
        items = []
        holdingArtists = {}
        for i in searchTemp['artists']:
            holdingArtists[i['name']] = i['id']
        items.append(objects.Track(i['id'], holdingArtists, i['available_markets'], i['disc_number'], i['duration_ms'],
                                   i['explicit'], None, i['external_urls'], i['href'], i['id'], i['name'], None,
                                   i['preview_url'], i['track_number'], i['type'], i['uri'], None))
    else:
        items = {}
        for i in searchTemp[type]['items']:
            items[i['name']]: i['id']

    return objects.PagingObject(searchTemp[type]['href'], items, searchTemp[type]['limit'], searchTemp[type]['next'],
                                searchTemp[type]['offset'], searchTemp[type]['previous'], searchTemp[type]['total'])


################
# Episodes API # IGNORE THESE FUNCTIONS FOR NOW.
################

def getAnEpisode(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("",
                                 headers={'Authorization': 'Bearer ' + access_token})
    info = starting_info.json()
    return 0

def getManyEpisodes(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("",
                                 headers={'Authorization': 'Bearer ' + access_token})
    info = starting_info.json()
    return 0


#######################
# Personalization API #
#######################

def getUsersTopArtistsandTrack(refresh_token, client_id, client_secret, type, num=20, start=0):
    if num > 50:
        num = 50
    if num < 1:
        num = 1
    if start < 0:
        start = 0
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    starting_info = requests.get("https://api.spotify.com/v1/me/top/%s" % type,
                                 headers={'Authorization': 'Bearer ' + access_token},
                                 params={'limit': num, 'offset': start})
    info = starting_info.json()
    list_of_items = []
    if type == 'artists':
        for artist in info['items']:
            list_of_images = []
            for image in artist['images']:
                list_of_images.append(image['url'])
            list_of_items.append(objects.Artist(artist['external_urls'], artist['followers']['total'], artist['genres'],
                                                artist['href'], artist['id'], list_of_images, artist['name'],
                                                artist['popularity'], artist['type'], artist['uri']))
    elif type == 'tracks':
        for track in info['items']:
            artist_dict = {}
            for artist in track['artists']:
                artist_dict[artist['name']]: artist['id']
            list_of_items.append(objects.Track(track['album']['id'], artist_dict, track['available_markets'],
                                               track['disc_number'], track['duration_ms'], track['explicit'],
                                               track['external_ids'], track['external_urls'], track['href'],
                                               track['id'], track['name'], track['popularity'], track['preview_url'],
                                               track['track_number'], track['type'], track['uri'], None))
    paging_obj = objects.PagingObject(info['href'], list_of_items, info['limit'], info['next'], info['offset'],
                                      info['previous'], info['total'])
    return paging_obj

##############
# Player API #
##############

#Done by Scott, Someone check and test these please, comment if it does/doesn't work and notify me of my errors please

def skipUserPlayback(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    skipCheck = requests.post('https://api.spotify.com/v1/me/next',
                            headers={'Authorization': 'Bearer ' + access_token})
    return skipCheck


def setRepeat(refresh_token, client_id, client_secret, state):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    repeatCheck = requests.put("https://api.spotify.com/v1/me/player/repeat",
    headers={'authorization': 'Bearer' +access_token},
                              params={'state':state})
    return repeatCheck

def userPlaybackDeviceTransfer(refresh_token, client_id, client_secret, device_ids):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    userDevicePlaybackCheck = requests.put("https://api.spotify.com/v1/me/player",
                                           headers={'authorization': 'Bearer' +access_token},
                                           params={'device_ids':device_ids})
    #Somethings missing here in PlaybackDeviceTransfer.....###
    return userDevicePlaybackCheck


def getUserCurrentPlayingTrack(refresh_token, client_id, client_secret, market):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    userCurrentTrack = requests.get("https://api.spotify.com/v1/me/player/currently-playing",
                                       headers={'authorization':'Bearer' +access_token},
                                       params={'market':market})
    playingTrackList=[]
    currentTrack= userCurrentTrack.json()
    trackDict={}
    for t in currentTrack:
            playingTrackList.append(objects.Track(t['album']['id'], trackDict, t['available_markets'],
                                               t['disc_number'], t['duration_ms'], t['explicit'],
                                               t['external_ids'], t['external_urls'], t['href'],
                                               t['id'], t['name'], t['popularity'], t['preview_url'],
                                               t['track_number'], t['type'], t['uri'], None))
            return objects.Track
    ###getUserCurrentPLayingTrack isn't going to work and I don't know why, (Scott)


def seekToTrackPosition(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    seekToTrackPos = requests.put("https://api.spotify.com/v1/me/player/seek",
                                    headers={'authorization': 'Bearer' + access_token})
    return seekToTrackPos



def skipToPreviousTrack(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    skipToPreviousSong = requests.post("https://api.spotify.com/v1/me/player/previous",
                                  headers={'authorization': 'Bearer' + access_token})
    return skipToPreviousSong

def startUserPlayback(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    play = requests.put("https://api.spotify.com/v1/me/player/play",
                                       headers={'authorization': 'Bearer' + access_token})
    return play



def stopUserPlayback(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    pause = requests.put("https://api.spotify.com/v1/me/player/pause",
                        headers={'authorization': 'Bearer' + access_token})
    return pause

def setUserVolume(refresh_token, client_id, client_secret, volume_percent):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    volumeSet= requests.put("https://api.spotify.com/v1/me/player/volume",
                            {'authorization': 'Bearer' + access_token},
                            params={'volume_percent' :volume_percent})
    return volumeSet
####This one I did not handle the integer (Between 1 & 100) correctly for the volume setting parameter, I don't think it should be a string {Scott}


def recentlyPlayedTracks(refresh_token, client_id, client_secret):
    access_token = getAccessToken(refresh_token, client_id, client_secret)
    recentHistory=












