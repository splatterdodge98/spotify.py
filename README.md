# spotify.py
A wrapper for the Spotify Web API built for python.
https://developer.spotify.com/documentation/web-api/reference/


# Classes:

Album: Corresponds to the Album JSON object given in the Spotify Web API documents, with some types omitted for simplicity's sake. Listed below are the object's attributes and their corresponding types:
  1. albumType: String. What "type" of album it is, "single", "album", or "compilation".
  2. artists: Dictionary of artists on the album, with the key being the name and the id being the value ({name:id})
  3. 
  
  
Artist: Corresponds to the Album JSON Object given in the Spotify Web API documents, as well as the simplified version. Listed below are the object's attributes and their corresponding types:
    1. externalURLs: 2-String Dictionary of URLs for the artist, with the key being the 'location' (eg: Spotify/ITunes/etc.) and the actual url being the value. ({location:url})
    2. followers: Integer. Number of followers this artist has.
    3. genres: String Array. Each string is a genre that the artist is associated with.
    4. href: String. A url linking to the Web API's Spotify information about the Artist.
    5. artistId: String. The Spotify ID for the Artist.
    6. images: List<String>. Each string is a url to an image associated with the Artist.
    7. artistName: String. The name of the artist.
    8. popularity: Integer. A value ranging from 0-100, with a higher value being a higher overall popularity, which is calulated by Spotify by all of the artist's tracks.
    9. type: String. The JSON Object type, which should always return "artist".
    10. userUri: String. The Spotify URI for the artist.
    
    
CurrentlyPlayingObject: Corresponds to the CurrentlyPlayingObject JSON Object given in the Spotify Web API documents. Listed below are the object's attributes and their corresponding types:
    1. context: A ContextObject(? Send halp plz)
    2. currentlyPlayingType: String. The object Type of whatever item is currently playing; either "track", "episode", "ad", or "unknown".
    3. isPlaying: Boolean. Returns true if something is playing, false otherwise.
    4. item: String. The currently playing track. Can potentially be None.
    5. progressMs: Integer. The progress into the currently playing track, in milliseconds. Can potentially be None.
    6. timestamp: Integer. The Unix millisecond Timestamp as to when the data was obtained.


DeviceObject: Corresponds to the DeviceObject JSON Object given in the Spotify Web API documents. Listed below are the object's attributes and their corresponding types:
    1. deviceId: String. The ID of the device playing Spotify. Can potentially be None.
    2. isActive: Boolean. Returns true if the deivce is currently the active device, false otherwise.
    3. isPrivateSession: Boolean. Returns true if the current session is private, false otherwise.
    4. isRestricted: Boolean. Returns true if the device will not accept Web API commands, false otherwise.
    5. name: String. The name of the device.
    6. type: String. The type of the device, eg: "Computer", "Smartphone", "Speaker", etc.
    7. volumePercent: Integer. The current volume, in a percentage (eg: 75 = 75%). Can potentially be None.
    
    
PlaylistObject: Corresponds to the Playlist JSON Object given in the Spotify Web API documents, as well as the simplified version. Listed below are the object's attributes and their corresponding types:
    1. collaborative: Boolean. Returns true if the owner allows other users to modify the Playlist, false otherwise.
    2. externalUrls: 2-String Dictionary of URLs for the playlist, with the key being the 'location' (eg: Spotify/ITunes/etc.) and the actual url being the value. ({location:url})
    3. href: String. A url linking to the Web API's Spotify information about the Playlist.
    4. playlistId: String. The Spotify ID for the Playlist.
    5. images: List<String>. Each string is a url to an image associated with the Playlist.
    6. name: String. The name of the Playlist.
    7. owner: 2-String Dictionary. The key is the name of the owner, while the value is their Spotify ID. ({name:id})
    8. public: Boolean. Returns true if the playlist is public, false if it is private, and None if it is not relevant.
    9. snapshotId: String. The version ID for the playlist. Used to help target a specific version of a playlist.
    10. tracks: 2-String Dictionary. The key is the name of the track, whereas the value is the track's Spotify ID ({name:id}).
    11. type: String. The JSON Object tpe, which should always return "playlist".
    12. uri: String. The Spotify URI for the playlist.