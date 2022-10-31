from hmac import new
from album.api.v1.serializers import AlbumSerializer, serializers
from django.test import TestCase
from collections import OrderedDict


RAW_REPRESENTATION = OrderedDict(
    [
        ("album", "Fallen Leaves[2015]"),
        ("name", "Fallen Leaves"),
        ("artist_name", "Billy Talent"),
        ("tracks", ["Man alive", "Fallen leaves"]),
    ]
)

RAW_REPRESENTATION_DIFFERENT_FIELD_NAMES = OrderedDict(
    [
        ("album", "Fallen Leaves[2015]"),
        ("name", "Fallen Leaves"),
        ("different_name", "Billy Talent"),
        ("tracks", ["Man alive", "Fallen leaves"]),
    ]
)

RAW_FIELDS_1 = OrderedDict(
    [
        ("album", serializers.StringRelatedField(read_only=True, source="__str__")),
        ("name", serializers.CharField(label="Название альбома", max_length=100)),
        ("artist_name", serializers.StringRelatedField(source="artist.name")),
        (
            "tracks",
            serializers.ManyRelatedField(
                child_relation=serializers.StringRelatedField()
            ),
        ),
    ]
)

RAW_FIELDS_2 = OrderedDict(
    [
        ("album", serializers.StringRelatedField(read_only=True, source="album.name")),
        ("name", serializers.CharField(label="Название альбома", max_length=100)),
        ("different_name", serializers.StringRelatedField(source="artist.name.year")),
        (
            "tracks",
            serializers.ManyRelatedField(
                child_relation=serializers.StringRelatedField()
            ),
        ),
    ]
)

RESULT_1 = OrderedDict(
    [
        ("album", "Fallen Leaves[2015]"),
        ("name", "Fallen Leaves"),
        ("tracks", ["Man alive", "Fallen leaves"]),
        ("artist@name", "Billy Talent"),
    ]
)

RESULT_2 = OrderedDict(
    [
        ("name", "Fallen Leaves"),
        ("tracks", ["Man alive", "Fallen leaves"]),
        ("album@name", "Fallen Leaves[2015]"),
        ("artist@name@year", "Billy Talent"),
    ]
)


class TestSerializerMethod(TestCase):
    def test_rename_function(self):

        new_fields = AlbumSerializer.rename_fields(
            RAW_FIELDS_1.items(), RAW_REPRESENTATION
        )

        self.assertEqual(new_fields, RESULT_1)
        self.assertFalse(new_fields is RAW_REPRESENTATION)

        new_fields = AlbumSerializer.rename_fields(
            RAW_FIELDS_2.items(), RAW_REPRESENTATION_DIFFERENT_FIELD_NAMES
        )
        self.assertEqual(new_fields, RESULT_2)
