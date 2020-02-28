# spotify.py
A wrapper for the Spotify Web API built for python.
https://developer.spotify.com/documentation/web-api/reference/


# Objects:
Album: Corresponds to the Album JSON object given the Spotify Web API docs, some types ommitted for simplicities sake. listed beloew are the objects attributes and their corresponding types:
  1. albumType: What "type" of album it is, "single", "album", or "compilation"
  2. artists: Dictionary of artists on the album, with the key being the name and the id being the value ({name:id})
  3. 
