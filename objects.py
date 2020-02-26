class Album:

    def __init__(self, albumType, artists, externalIds, externalUrls, genres, albumId, images, name, releaseDate,
                 tracks, URI):
        self.albumType = albumType  # String type
        self.artists = artists  # List of Names of the Artists
        self.externalIds = externalIds  # ExternalID Object
        self.externalUrls = externalUrls  # ExternalURLS Object
        self.genres = genres  # list of strings
        self.albumId = albumId  # String
        self.images = images  # Url for the image
        self.name = name  # String
        self.releaseDate = releaseDate  # String that we'll convert to DateTime
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

    def __init__(self, href, items, limit, nextPage, cursors, total):
        self.href = href #String
        self.items = items #Array of Objects (Unsure what kind)
        self.nextPage = nextPage #String (URL of next page)
        self.cursors = cursors #String (Cursor Object)
        self.total = total #Integer

class PublicUserObject:

    def __init__(self, displayName, externalUrls, followers, href, userPublicObjectId, userProfileImages, userType, userUri):
        self.displayName = displayName # (String)	The name displayed on the user’s profile. null if not available.
        self.extrnalUrls = externalUrls # (external URL Object) Known public external URLs for this user
        self.followers = followers # (a followers object) Information about the followers of this user
        self.href = href # (String) 	A link to the Web API endpoint for this user.
        self.userPublicObjectId = userPublicObjectId # (String) The Spotify user ID for this user.
        self.userPublicProfileImages = userProfileImages #(Array of image objects) The users profile image
        self.userType = userType #(string) The object type "user"
        self.userUri = userUri #(String) The Spotify URI for this user

class Artist:

    def __init__(self, externalUrls, followers, genres, href, artistId, images, artistName, popularity, type, uri):
        self.externalUrls = externalUrls #Dictionary of Size 1 (External URL Object)
        self.followers = followers #Dictionary of Size 1
        self.genres = genres #String Array
        self.href = href #String
        self.artistId = artistId #String
        self.images = images #List<String> of image urls
        self.artistName = artistName #String
        self.popularity = popularity #Integer, btwn 0-100
        self.type = type #String. Type of the object (artist).
        self.uri = uri #String

class CurrentlyPlayingObject:

    def __init__(self, context, currentlyPlayingType, isPlaying, item, progressMs, timestamp):
        self.context = context #ContextObject
        self.currentlyPlayingType = currentlyPlayingType #String. Type of item playing; either track, episode, ad, or unknown
        self.isPlaying = isPlaying #Boolean.
        self.item = item #String ID of the Track Object.
        self.progressMs = progressMs #Integer. Progress in current track, can be null
        self.timestamp = timestamp #integer. Time when fetched.

class DeviceObject:

    def __init__(self, deviceId, isActive, isPrivateSession, isRestricted, name, type, volumePercent):
        self.deviceId = deviceId #String. ID of the device, may be null
        self.isActive = isActive #Boolean. Is this device currently active or not
        self.isPrivateSession = isPrivateSession #Boolean.
        self.isRestricted = isRestricted #Boolean. True, no API commands allowed
        self.name = name #String. Name of the device
        self.type = type #String. Type of device running Spotify
        self.volumePercent = volumePercent #Integer. Current Volume in percentage. May be null.

class PlaylistObject:

    def __init__(self, collaborative, externalUrls, href, playlistId, images, name, owner, public, snapshotId, tracks, type, uri):
        self.collaborative = collaborative #Boolean. True means others can modify playlist
        self.externalUrls = externalUrls #2 String Dictionary. {location:url} structure.
        self.href = href #String. link to the Web API version of the playlist
        self.playlistId = playlistId #String.
        self.images = images #List<String> of the urls for each image
        self.name = name #String. Name of the playlist
        self.owner = owner #2 String Dictionary. {Name:ID} structure.
        self.public = public #Boolean
        self.snapshotId = snapshotId #String. Version id of the playlist
        self.tracks = tracks #2 String Dictionary of each track, {name:id} structure.
        self.type = type #String. The type of the object, playlist
        self.uri = uri #String

class PrivateUserObject:

    def __init__(self, country, displayName, email, externalUrls, followers, href, userId, images, product, type, uri):
        self.country = country #String. ISO 3166-1 alpha country code
        self.displayName = displayName #String.
        self.email = email #String.
        self.externalUrls = externalUrls #2 String Dictionary {location:url} structure
        self.href = href #Striing. Link to Web API endpoint
        self.userId = userId #String.
        self.images = images #List<String> of the urls for each image
        self.product = product #String. Spotify subscription level. May be null
        self.type = type #String. Object typ: user
        self.uri = uri #String

class Category:

    def __init__(self, href, icons, id, name):
        self.href = href # String type
        self.icons = icons # List of images
        self.id = id # String type
        self.name = name # String type


class SavedAlbum:

    def __init__(self, albumType, artists, externalIds, externalUrls, genres, albumId, images, name, releaseDate,
                 tracks, timestamp, URI):
        self.albumType = albumType  # String type
        self.artists = artists  # List of Names of the Artists
        self.externalIds = externalIds  # ExternalID Object
        self.externalUrls = externalUrls  # ExternalURLS Object
        self.genres = genres  # list of strings
        self.albumId = albumId  # String
        self.images = images  # Url for the image
        self.name = name  # String
        self.releaseDate = releaseDate  # String that we'll convert to DateTime
        self.tracks = tracks  # Dictionary with {name:id} structure
        self.timestamp = timestamp # datetime type
        self.URI = URI  # string

class ExternalId:

    def __init__(self, ean, isrc, upc):
        self.ean = ean # string
        self.isrc = isrc # string
        self.upc = upc # string
        
class TrackObject:
    
    def __init__(self, albumId, artists, availableMarkets, discNum, durationMs, explicit, externalIds, externalUrls, 
                 href, trackId, isPlayable, linkedFrom, restrictions, name, popularity, previewUrl, trackNum, type, uri, isLocal)
    self.albumId = albumId #String
    self.artists = artists #List of Artist Names (Strings)
    self.availableMarkets = availableMarkets #List of Strings. Identifies each country in which the track is available
    self.discNum = discNum #Integer. On which disc is the track
    self.durationMs = durationMs #Integer. Track length in ms
    self.explicit = explicit #Boolean. Is the track explicit or not
    self.externalIds = externalIds #String Dictionary of Size 2 (External ID Object)
    self.externalUrls = externalUrls #String Dictionary of Size 2 (External URL Object)
    self.href = href #String.
    self.trackId = trackId #String
    self.isPlayable = isPlayable #Boolean
    self.linkedFrom = linkedFrom #String(?) Same as href???
    self.restrictions = restrictions #String Dictionary of Size 2. Structure of: {"restrictions" : {"reason" : "market"}}
    self.name = name #String
    self.popularity = popularity #Integer. Value btwn 0-100
    self.previewUrl = previewUrl #String. Link to a preview
    self.trackNum = trackNum #Integer
    self.type = type #String. Object type (track)
    self.uri = uri #String
    self.isLocal = isLocal #Boolean
    
