# spotify.py
A wrapper for the Spotify Web API built for python.
https://developer.spotify.com/documentation/web-api/reference/


# Classes:

Album: Corresponds to the Album JSON object given in the Spotify Web API documents, with some types omitted for simplicity's sake. Listed below are the object's attributes and their corresponding types:
    1. albumType: String. What "type" of album it is, "single", "album", or "compilation".
    2. artists: Dictionary of artists on the album, with the key being the name and the id being the value ({name:id})
    3. externalIds: A reference to the ExternalID Object, which contains all of the IDs for the associated Album.
    4. externalUrls: 2-String Dictionary. URLs for the album, with the key being the 'location' (eg: Spotify/ITunes/etc.) and the actual url being the value. ({location:url})
    5. genres: String Array. Each string is a genre that the album is associated with.
    6. List<String>. Each string is a URL to an image associated with the album.
    7. name: String. The name of the album.
    8. releaseDate: DateTime. CThe Date and Time an album was released, with a structure of: (YYYY-MM-DD HH:MM:SS.SSZ)
    9. tracks: 2-String Dictionary. Contains all of the tracks associated with the dictionary, with their name being the key, and id being the value. Show here iis the structure: ({name:id})
    10. URI: String. The Spotify URI for the Album.
  
  
Artist: Corresponds to the Album JSON Object given in the Spotify Web API documents, as well as the simplified version. Listed below are the object's attributes and their corresponding types:
    1. externalURLs: 2-String Dictionary. URLs for the artist, with the key being the 'location' (eg: Spotify/ITunes/etc.) and the actual url being the value. ({location:url})
    2. followers: Integer. Number of followers this artist has.
    3. genres: String Array. Each string is a genre that the artist is associated with.
    4. href: String. A URL linking to the Web API's Spotify information about the Artist.
    5. artistId: String. The Spotify ID for the Artist.
    6. images: List<String>. Each string is a URL to an image associated with the Artist.
    7. artistName: String. The name of the artist.
    8. popularity: Integer. A value ranging from 0-100, with a higher value being a higher overall popularity, which is calulated by Spotify by all of the artist's tracks.
    9. type: String. The JSON Object type, which should always return "artist".
    10. userUri: String. The Spotify URI for the Artist.
    
    
CurrentlyPlayingObject: Corresponds to the CurrentlyPlayingObject JSON Object given in the Spotify Web API documents. Listed below are the object's attributes and their corresponding types:
    1. context: 2-String Dictionary. Contains the href, type, and uri for the context of whatever is currently playing. ({'href':'url', 'type':'context', 'uri':'url'})
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
    2. externalUrls: 2-String Dictionary. URLs for the playlist, with the key being the 'location' (eg: Spotify/ITunes/etc.) and the actual url being the value. ({location:url})
    3. href: String. A URL linking to the Web API's Spotify information about the Playlist.
    4. playlistId: String. The Spotify ID for the Playlist.
    5. images: List<String>. Each string is a URL to an image associated with the Playlist.
    6. name: String. The name of the Playlist.
    7. owner: 2-String Dictionary. The key is the name of the owner, while the value is their Spotify ID. ({name:id})
    8. public: Boolean. Returns true if the playlist is public, false if it is private, and None if it is not relevant.
    9. snapshotId: String. The version ID for the playlist. Used to help target a specific version of a playlist.
    10. tracks: 2-String Dictionary. The key is the name of the track, whereas the value is the track's Spotify ID ({name:id}).
    11. type: String. The JSON Object tpe, which should always return "playlist".
    12. uri: String. The Spotify URI for the Playlist.
    
    
PrivateUserObject: Corresponds to the PrivateUserObject JSON Object given in the Spotify Web API documents, with some types omitted for simplicity's sake. Listed below are the object's attributes and their corresponding types:
    1. country: String. The ISO 3166-1 aplha-2 country code set by the user.
    2. displayName: String. The name displayed on the user's profile. Can potentially be None.
    3. email: String. The email address set by the user. There is no proof this actually belongs to the user, so use with caution.
    4. externalUrls: 2-String Dictionary. Known URLs for the user, with the key being the 'location' (eg: Spotify/ITunes/etc.) and the actual url being the value. ({location:url})
    5. href: String. A URL linking to the Web API's Spotify information about the User.
    6. userId: String. The Spotify ID for the user.
    7. images: List<String>. Each string is a URL to an image associated with the Playlist.
    8. product: String. The user's Spotify subscription level. Can be "premium", "free", "open", etc.
    9. type: String. The JSON Object tpe, which should always return "user".
    10. userUri: String. The Spotify URI for the User.
    
    
Track: Corresponds to the TrackObject JSON Object given in the Spotify Web API documents, with some types modified for simplicity's sake. Listed below are the object's attributes and their corresponding types:
    1. albumId: String. The Spotify ID of the album the track is on.
    2. artists: List<String>. Each String is an artist name who performs on the track.
    3. availableMarkets: List<String>. A list of the countries in which the track can be played, each identified by their ISO 3166-1 aplha-2 code.
    4. discNum: Integer. The disc on which the track is on (usually 1, may be more if an album contains >1 disc).
    5. durationMs: Integer. The langth of the track in milliseconds.
    6. explicit: Boolean. Returns true if the track is known to contain explicit lyrics, false otherwise.
    7. externalIds: A reference to the ExternalID Object, which contains all of the IDs for the associated Track.
    8. externalUrls: 2-String Dictionary. URLs for the track, with the key being the 'location' (eg: Spotify/ITunes/etc.) and the actual url being the value. ({location:url})
    9. href: String. A URL linking to the Web API's Spotify information about the Track.
    10. trackId: String. The Spotify ID for the Track.
    11. isPlayable: Boolean. Returns true if the Track is playable in the user's current market, false otherwise.
    12. linkedFrom: Sting. A URL linking to another version of the track that was unavailable in the user's current market.
    13. restrictions: 2-String Dictionary. Contains the restriction for the 'linkedFrom' track and their reasoning for each market. Key is the reason, and value is the market itself. ({"reason" : "market"})
    14. name: String. The name of the Track.
    15. popularity: Integer. A value ranging from 0-100, with a higher value being a higher overall popularity, which is calulated by Spotify.
    16. previewUrl: String. A URL linking to a 30-second preview of the track. Can potentially be None.
    17. trackNum: Integer. The number of the track on its album. If an album has several discs, the track number specifically on that disc (eg: A track can have discNum = 2, trackNum = 1.)
    18. type: String. The JSON Object tpe, which should always return "track".
    19. uri: String. The Spotify URI for the Track.
    20. isLocal: Boolean. Returns true if the track is from a local file, false otherwise.
    
    
SavedTrack: Corresponds to the TrackObject JSON Object given in the Spotify Web API documents, with some types modified for simplicity's sake. Listed below are the object's attributes and their corresponding types:
    1. albumId: String. The Spotify ID of the album the track is on.
    2. artists: List<String>. Each String is an artist name who performs on the track.
    3. availableMarkets: List<String>. A list of the countries in which the track can be played, each identified by their ISO 3166-1 aplha-2 code.
    4. discNum: Integer. The disc on which the track is on (usually 1, may be more if an album contains >1 disc).
    5. durationMs: Integer. The langth of the track in milliseconds.
    6. explicit: Boolean. Returns true if the track is known to contain explicit lyrics, false otherwise.
    7. externalIds: A reference to the ExternalID Object, which contains all of the IDs for the associated Track.
    8. externalUrls: 2-String Dictionary. URLs for the track, with the key being the 'location' (eg: Spotify/ITunes/etc.) and the actual url being the value. ({location:url})
    9. href: String. A URL linking to the Web API's Spotify information about the Track.
    10. trackId: String. The Spotify ID for the Track.
    11. isPlayable: Boolean. Returns true if the Track is playable in the user's current market, false otherwise.
    12. linkedFrom: Sting. A URL linking to another version of the track that was unavailable in the user's current market.
    13. restrictions: 2-String Dictionary. Contains the restriction for the 'linkedFrom' track and their reasoning for each market. Key is the reason, and value is the market itself. ({"reason" : "market"})
    14. name: String. The name of the Track.
    15. popularity: Integer. A value ranging from 0-100, with a higher value being a higher overall popularity, which is calulated by Spotify.
    16. previewUrl: String. A URL linking to a 30-second preview of the track. Can potentially be None.
    17. trackNum: Integer. The number of the track on its album. If an album has several discs, the track number specifically on that disc (eg: A track can have discNum = 2, trackNum = 1.)
    18. type: String. The JSON Object tpe, which should always return "track".
    19. uri: String. The Spotify URI for the Track.
    20. isLocal: Boolean. Returns true if the track is from a local file, false otherwise.
    21. timestamp: DateTime. The date and time at which the track was saved, in ISO 8601 format, ie: (YYYY-MM-DDTHH:MM:SSZ). May be imprecise.
    
AudioFeatureObject: orresponds to the Audio Features JSON Object given in the Spotify Web API documents, with some types modified for simplicity's sake. Listed below are the object's attributes and their corresponding types:
    1. acousticness: Float. A value from 0.0 to 1.0, measuring how acoustic the track is. A higher value means it is more likely acoustic.
    2. analysisUrl: String. A URL with access to the full audio analysis of the track. An access token is required to be able to use this.
    3. danceability: Float. A value from 0.0 to 1.0, measuring how danceable the track is. A higher value means the track is more danceable.
    4. durationMS: Integer. The duration of the track in milliseconds.
    5. energy: Float. A value from 0.0 to 1.0 that measures the intesity of the track. A higher value means the track is mroe intense.
    6. trackId: String. The Spotify ID for the Track.
    7. instrumentalness: Float. A value from 0.0 to 1.0 to predict whether the track contains vocals or not. A value of 0.5 or higher is intended to represent instrumental tracks, with higher values meaning fewer vocals.
    8. key: Integer. The music key that the Track is in, using standard Ptch Class Notation. (EG: C = 0, C# = 1, D = 2, etc.)
    9. liveness: Float. A value from 0.0 to 1.0 that measures the chance that there is an audience in the track. A higher value means there is a greater chance, with values at or above 0.8 meaning there is an almost certain chance there is an audience (and the track is being performed live).
    10. loudness: Float. The overall loudness of the track in decibels. Values typically range between -60 and 0 db.
    11. mode: Integer. Determines whether a track is in a Major Key or Minor Key. 1 is Major, 0 is Minor.
    12. speechiness: Float. A value between 0.0 and 1.0 that determines how much normal speech is in the track. Values below 0.33 likely have almost no spoken lines, values between 0.33 and 0.66 may be more of a mix of the two (see: rap), and values above 0.66 likely contain only spoken words. A higher value means there are more spoken words and fewer sung words.
    13. tempo: Float. The overall estimated tempo of the track in Beats per Minute (BPM). A higher values means an overall faster track.
    14. timeSignature: Integer. An overall estimated value of the track's time signature. The time signature is a convention used to determine how many beats are in a single measure (bar).
    15. trackHref: String. A link to the Web API endpoint for the full details of the Track.
    16. type: String. The JSOn Object Type, which should always return "audio_features".
    17. uri: String. The Spotify URi for the Track.
    18. valence: Float. A value between 0.0 and 1.0 describing the overall positiveness of the track. A higher value means that the track feels more positive overall.