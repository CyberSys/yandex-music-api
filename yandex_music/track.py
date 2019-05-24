from yandex_music import YandexMusicObject


class Track(YandexMusicObject):
    def __init__(self,
                 id,
                 title,
                 available,
                 available_for_premium_users,
                 artists,
                 albums,
                 lyrics_available,
                 real_id=None,
                 og_image=None,
                 type=None,
                 cover_uri=None,
                 major=None,
                 duration_ms=None,
                 storage_dir=None,
                 file_size=None,
                 normalization=None,
                 error=None,
                 regions=None,
                 available_as_rbt=None,
                 content_warning=None,
                 explicit=None,
                 client=None,
                 **kwargs):
        self.id = id
        self.title = title
        self.available = available
        self.available_for_premium_users = available_for_premium_users
        self.artists = artists
        self.albums = albums
        self.lyrics_available = lyrics_available

        self.real_id = real_id
        self.og_image = og_image
        self.type = type
        self.cover_uri = cover_uri
        self.major = major
        self.duration_ms = duration_ms
        self.storage_dir = storage_dir
        self.file_size = file_size
        self.normalization = normalization
        self.error = error
        self.regions = regions
        self.available_as_rbt = available_as_rbt
        self.content_warning = content_warning
        self.explicit = explicit

        self.download_info = None

        self.client = client
        self._id_attrs = (self.id,)

    def get_download_info(self, get_direct_links=False):
        self.download_info = self.client.tracks_download_info(self.track_id, get_direct_links)

        return self.download_info

    def download_cover(self, filename):
        self.client._request.download(self.cover_uri, filename)

    def download(self, filename, codec='mp3', bitrate_in_kbps=192):
        if self.download_info is None:
            self.get_download_info()

        for info in self.download_info:
            if info.codec == codec and info.bitrate_in_kbps == bitrate_in_kbps:
                info.download(filename)

    @property
    def track_id(self):
        return f'{self.id}'

    @classmethod
    def de_json(cls, data, client):
        if not data:
            return None

        data = super(Track, cls).de_json(data, client)

        return cls(client=client, **data)

    @classmethod
    def de_list(cls, data, client):
        if not data:
            return []

        tracks = list()
        for track in data:
            tracks.append(cls.de_json(track, client))

        return tracks
