class album:

    def __init__(self, albumType, artists, externalIds, externalUrls, genres, album_id, images, name, releaseDate,
                 tracks, URI):
        self.albumType = albumType  # String type
        self.artists = artists  # List of Names of the Artists
        self.externalIds = externalIds  # ExternalID Object
        self.externalUrls = externalUrls  # ExternalURLS Object
        self.genres = genres  # list of strings
        self.album_id = album_id  # String
        self.images = images  # Url for the image
        self.name = name  # String
        self.releaseDate = releaseDate  # String that we'll convert to DateTime
        self.tracks = tracks  # Dictionary with {name:id} structure
        self.URI = URI  # string


class RecommendationSeedObject:

    def __init__(self, initialPoolSize, afterFilterSize, afterRelinkingSize, href, recomendation_id,
                 recomendation_type):
        self.init_pool_size = initialPoolSize #Integer
        self.after_filter_size = afterFilterSize #Integer
        self.after_relegation_size = afterRelinkingSize #Integer
        self.href = href #String
        self.recomendation_id = recomendation_id #String
        self.recomendation_type = recomendation_type #String


class ContextObject:
    def __init__(self, uri, href, external_urls, context_type, ):
        self.uri = uri #String
        self.href = href #String
        self.external_urls = external_urls #String Dictionary of Size 2 (External URL Object)
        self.context_type = context_type #String


class CursorBasedPagingObject:
    def __init__(self, href, items, limit, next_page, cursors, total, ):
        self.href = href #String
        self.items = items #Array of Objects (Unsure what kind)
        self.next_page = next_page #String (URL of next page)
        self.cursors = cursors #String (Cursor Object)
        self.total = total #Integer

class PublicUserObject:
    def __init__(self, display_name, external_urls, followers, href, user_public_object_id, user_profile_images, user_type, user_uri):
        self.display_name = display_name # (String)	The name displayed on the user’s profile. null if not available.
        self.extrnal_urls = external_urls # (external URL Object) Known public external URLs for this user
        self.followers = followers # (a followers object) Information about the followers of this user
        self.href = href # (String) 	A link to the Web API endpoint for this user.
        self.user_public_object_id = user_public_object_id # (String) The Spotify user ID for this user.
        self.user_public_profile_images = user_profile_images #(Array of image objects) The users profile image
        self.user_type = user_type #(string) The object type "user"
        self.user_uri = user_uri #(String) The Spotify URI for this user hi

class Artist:
    def __init__(self, external_urls, followers, genres, href, artist_id, images, artist_name, popularity, type, uri):
        self.external_urls = external_urls #Dictionary of Size 1 (External URL Object)
        self.followers = followers #Dictionary of Size 1
        self.genres = genres #String Array
        self.href = href #String
        self.artist_id = artist_id #String
        self.images = images #List<String> of image urls
        self.artist_name = artist_name #String
        self.popularity = popularity #Integer, btwn 0-100
        self.type = type #String. Type of the object (artist).
        self.uri = uri #String


class category:

    def __init__(self, href, icons, id, name):
        self.href = href # String type
        self.icons = icons # List of images
        self.id = id # String type
        self.name = name # String type


class SavedAlbum:

    def __init__(self, albumType, artists, externalIds, externalUrls, genres, album_id, images, name, releaseDate,
                 tracks, timestamp, URI):
        self.albumType = albumType  # String type
        self.artists = artists  # List of Names of the Artists
        self.externalIds = externalIds  # ExternalID Object
        self.externalUrls = externalUrls  # ExternalURLS Object
        self.genres = genres  # list of strings
        self.album_id = album_id  # String
        self.images = images  # Url for the image
        self.name = name  # String
        self.releaseDate = releaseDate  # String that we'll convert to DateTime
        self.tracks = tracks  # Dictionary with {name:id} structure
        self.timestamp = timestamp # datetime type
        self.URI = URI  # string