class album:

    def __init__(self, albumType, artists, externalIds, externalUrls, genres, id, images, name, releaseDate, tracks, URI):
        self.albumType = albumType #String type
        self.artists = artists #List of Names of the Artists
        self.externalIds = externalIds #ExternalID Object
        self.externalUrls = externalUrls #ExternalURLS Object
        self.genres = genres #list of strings
        self.id = id #String
        self.images = images #Url for the image
        self.name = name #String
        self.releaseDate = releaseDate #String that we'll convert to DateTime
        self.tracks = tracks #Dictionary with {name:id} structure
        self.URI = URI #string