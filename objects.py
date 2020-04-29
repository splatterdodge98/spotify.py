class Album:

    def __init__(self, albumType, artists, externalIds, externalUrls, genres, albumId, images, name, releaseDate, tracks, URI):
        self.albumType = albumType  # String type
        self.artists = artists  # Dictionary name:id pair
        self.externalIds = externalIds  # Dictionary
        self.externalUrls = externalUrls  # dictionary of spotify url
        self.genres = genres  # list of strings
        self.albumId = albumId  # String
        self.images = images  #List of image urls
        self.name = name  # String
        self.releaseDate = releaseDate  # String
        self.tracks = tracks  # Dictionary with {name:id} structure
        self.URI = URI  # string


class RecommendationSeedObject:

    def __init__(self, initialPoolSize, afterFilterSize, afterRelinkingSize, href, recomendationId,
                 recomendationType):
        self.initPoolSize = initialPoolSize #Integer
        self.afterFilterSize = afterFilterSize #Integer
        self.afterRelinkingSize = afterRelinkingSize #Integer
        self.href = href #String
        self.recomendationId = recomendationId #String
        self.recomendationType = recomendationType #String


class ContextObject:

    def __init__(self, uri, href, externalUrls, contextType):
        self.uri = uri #String
        self.href = href #String
        self.externalUrls = externalUrls #String Dictionary of Size 2 (External URL Object)
        self.contextType = contextType #String


class CursorBasedPagingObject:

    def __init__(self, href, items, nextPage, cursors, total):
        self.href = href #String
        self.items = items #Array of Objects (Unsure what kind)
        self.nextPage = nextPage #String (URL of next page)
        self.cursors = cursors #String (value of the sole entry in the dict that Spotify returns)
        self.total = total #Integer

class PublicUserObject:

    def __init__(self, displayName, externalUrls, followers, href, userPublicObjectId, userProfileImages, userType, userUri):
        self.displayName = displayName # (String)	The name displayed on the user’s profile. null if not available.
        self.extrnalUrls = externalUrls # (external URL Object) Known public external URLs for this user
        self.followers = followers # Int. Number of followers this user has.
        self.href = href # (String) 	A link to the Web API endpoint for this user.
        self.userPublicObjectId = userPublicObjectId # (String) The Spotify user ID for this user.
        self.userPublicProfileImages = userProfileImages #(List of image urls) The users profile image
        self.userType = userType #(string) The object type "user"
        self.userUri = userUri #(String) The Spotify URI for this user

class Artist:

    def __init__(self, externalUrls, followers, genres, href, artistId, images, artistName, popularity, type, userUri):
        self.externalUrls = externalUrls #2-String Dictionary
        self.followers = followers #Integer
        self.genres = genres #String Array
        self.href = href #String
        self.artistId = artistId #String
        self.images = images #List<String>
        self.artistName = artistName #String
        self.popularity = popularity #Integer, btwn 0-100
        self.type = type #String
        self.userUri = userUri #String

class CurrentlyPlayingObject:

    def __init__(self, context, currentlyPlayingType, isPlaying, item, progressMs, timestamp):
        self.context = context #2-String Dictionary
        self.currentlyPlayingType = currentlyPlayingType #String
        self.isPlaying = isPlaying #Boolean
        self.item = item #String
        self.progressMs = progressMs #Integer
        self.timestamp = timestamp #Integer

class DeviceObject:

    def __init__(self, deviceId, isActive, isPrivateSession, isRestricted, name, type, volumePercent):
        self.deviceId = deviceId #String
        self.isActive = isActive #Boolean
        self.isPrivateSession = isPrivateSession #Boolean
        self.isRestricted = isRestricted #Boolean
        self.name = name #String
        self.type = type #String
        self.volumePercent = volumePercent #Integer

class PlaylistObject:

    def __init__(self, collaborative, description, externalUrls, followers, href, playlistId, images, name, owner, public, snapshotId, tracks, type, uri):
        self.collaborative = collaborative #Boolean
        self.description = description #string
        self.externalUrls = externalUrls #2-String Dictionary
        self.followers = followers #int
        self.href = href #String
        self.playlistId = playlistId #String
        self.images = images #List<String>
        self.name = name #String.
        self.owner = owner #String.
        self.public = public #Boolean
        self.snapshotId = snapshotId #String
        self.tracks = tracks #2-String Dictionary
        self.type = type #String
        self.uri = uri #String

class PrivateUserObject:

    def __init__(self, country, displayName, email, externalUrls, followers, href, userId, images, product, type, userUri):
        self.country = country #String
        self.displayName = displayName #String
        self.email = email #String
        self.externalUrls = externalUrls #2-String Dictionary
        self.followers = followers #Int
        self.href = href #Striing
        self.userId = userId #String
        self.images = images #List<String>
        self.product = product #String
        self.type = type #String
        self.userUri = userUri #String

class Category:

    def __init__(self, href, icons, id, name):
        self.href = href # String type
        self.icons = icons # List of image urls
        self.id = id # String type
        self.name = name # String type


class SavedAlbum:

    def __init__(self, albumType, artists, externalIds, externalUrls, genres, albumId, images, name, releaseDate,
                 tracks, timestamp, URI):
        self.albumType = albumType  # String type
        self.artists = artists  # Dictionary {name: id}
        self.externalIds = externalIds  # ExternalID Object
        self.externalUrls = externalUrls  # ExternalURLS Object
        self.genres = genres  # list of strings
        self.albumId = albumId  # String
        self.images = images  # Url for the image
        self.name = name  # String
        self.releaseDate = releaseDate  # String
        self.tracks = tracks  # Dictionary with {name:id} structure
        self.timestamp = timestamp # datetime type
        self.URI = URI  # string

class ExternalId:

    def __init__(self, ean, isrc, upc):
        self.ean = ean # string
        self.isrc = isrc # string
        self.upc = upc # string
        
class Track:
    
    def __init__(self, albumId, artists, availableMarkets, discNum, durationMs, explicit, externalIds, externalUrls, href, trackId, name, popularity, previewUrl, trackNum, type, uri, isLocal):
        self.albumId = albumId #String
        self.artists = artists #Dictionary { name:id }
        self.availableMarkets = availableMarkets #List<String>
        self.discNum = discNum #Integer
        self.durationMs = durationMs #Integer
        self.explicit = explicit #Boolean
        self.externalIds = externalIds #Dictionary, { id_type: id }
        self.externalUrls = externalUrls #2-String Dictionary
        self.href = href #String
        self.trackId = trackId #String
        self.name = name #String
        self.popularity = popularity #Integer. Value btwn 0-100
        self.previewUrl = previewUrl #String
        self.trackNum = trackNum #Integer
        self.type = type #String
        self.uri = uri #String
        self.isLocal = isLocal #Boolean

class SavedTrack:
    
    def __init__(self, albumId, artists, availableMarkets, discNum, durationMs, explicit, externalIds, externalUrls, href, trackId, isPlayable, linkedFrom, restrictions, name, popularity, previewUrl, trackNum, type, uri, isLocal, timestamp):

        self.albumId = albumId #String
        self.artists = artists #List<String>
        self.availableMarkets = availableMarkets #List<String>
        self.discNum = discNum #Integer
        self.durationMs = durationMs #Integer
        self.explicit = explicit #Boolean
        self.externalIds = externalIds #Dictionary, { id_type: id }
        self.externalUrls = externalUrls #2-String Dictionary
        self.href = href #String.
        self.trackId = trackId #String
        self.isPlayable = isPlayable #Boolean
        self.linkedFrom = linkedFrom #String
        self.restrictions = restrictions #3-String Dictionary
        self.name = name #String
        self.popularity = popularity #Integer. Value btwn 0-100
        self.previewUrl = previewUrl #String
        self.trackNum = trackNum #Integer
        self.type = type #String
        self.uri = uri #String
        self.isLocal = isLocal #Boolean
        self.timestamp = timestamp #String

class AudioFeatureObject:

    def __init__(self, acousticness, analysisUrl, danceability, durationMS, energy, trackId, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, timeSignature, trackHref, type,
                 uri, valence):
        self.acousticness = acousticness #Float
        self.analysisUrl = analysisUrl #string
        self.danceability = danceability #Float
        self.durationMS = durationMS #int
        self.energy = energy #Float
        self.trackId = trackId #String
        self.instrumentalness = instrumentalness #float
        self.key = key #int
        self.liveness = liveness #float
        self.loudness = loudness #float
        self.mode = mode #int
        self.speechiness = speechiness #float
        self.tempo = tempo #float
        self.timeSignature = timeSignature #int
        self.trackHref = trackHref #string
        self.type = type #string
        self.uri = uri #string
        self.valence = valence

class PagingObject:

    def __init__(self, href, items, limit, nextItem, offset, previousItem, total):
        self.href = href #string
        self.items = items #this is gonna be a conversation tomorrow lol (???)
        self.limit = limit #int
        self.nextItem = nextItem #string
        self.offset = offset #int
        self.previousItem = previousItem #String
        self.total = total #int

class PlayHistoryObject:

    def __init__(self, context, playedAt, track):
        self.context = context #context object (?)
        self.playedAt = playedAt #DateTime
        self.track = track #Dictionary containing {name:id} structure

class PlaylistTrackObject:

    def __init__(self, addedAt, addedBy, isLocal, track):
        self.addedAt = addedAt #DateTime
        self.addedBy = addedBy #Public User Object (?)
        self.isLocal = isLocal
        self.track = track #dictionary containing {name:id} structure

class RecommendationsResponseObject:

    def __init__(self, seeds, tracks):
        self.seeds = seeds #list of recommendation seed objects
        self.tracks = tracks #list of track objects

class TuneableTrackObject:

    def __init__(self, acousticness, danceability, durationMS, energy, instrumentalness, key, liveness, loudness, mode, popularity, speechiness, tempo, timeSignature, valence):
        self.acousticness = acousticness #float
        self.danceability = danceability #float
        self.durationMS = durationMS #int
        self.energy = energy #float
        self.instrumentalness = instrumentalness #float
        self.key = key #int
        self.liveness = liveness #float
        self.loudness = loudness #float
        self.mode = mode #int
        self.popularity = popularity #float
        self.speechiness = speechiness #float
        self.tempo = tempo #float
        self.timeSignature = timeSignature #int
        self.valence = valence #float
