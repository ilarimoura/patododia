def fetch_text(metadata_line, metadata_type):
    if metadata_line['title'] == {'simpleText': metadata_type}:
        try:
            return metadata_line['defaultMetadata']['runs'][0]['text']
        except (KeyError, IndexError):
            try:
                return metadata_line['defaultMetadata']['simpleText']
            except (KeyError, IndexError):
                return None


class CorrectMetadata:
    song = None
    artist = None
    album = None

    def __init__(self, metadata):
        for metadata_line in metadata.__dict__['_raw_metadata']:
            if not self.song:
                self.song = fetch_text(metadata_line, 'SONG')

            if not self.artist:
                self.artist = fetch_text(metadata_line, 'ARTIST')

            if not self.album:
                self.album = fetch_text(metadata_line, 'ALBUM')

    def __str__(self):
        return f"{self.song} {self.artist} {self.album}"
