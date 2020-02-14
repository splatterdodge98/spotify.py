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
