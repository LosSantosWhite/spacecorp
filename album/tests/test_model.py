from django.test import TestCase

from album.models import Album, Artist, Track

TRACKS_LIST = ["Cut the curtains", "Fallen Leaves", "Man Alive"]


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        artist = Artist.objects.create(name="Billy Talent")
        album = Album.objects.create(name="Fallen leaves", artist=artist, year=2015)
        for track in TRACKS_LIST:
            Track.objects.create(name=track, album=album)

    def test_album_name(self):
        album_name = Album.objects.get(id=1)
        self.assertEqual(album_name.__str__(), "Fallen leaves[2015]")
