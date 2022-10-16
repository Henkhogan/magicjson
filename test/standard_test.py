from unittest import TestCase

from magicjson import MagicJson
from datetime import date, datetime, time

class StandardTestCase(TestCase):
    def test_init(self):
        MagicJson()

    def test_serialze_dict(self):

        mj = MagicJson()

        validation_dict = {
            'date': date(2000,1,1),
            'datetime': datetime(2010,11,12,13,14,15),
            'time': time(20,21,22),
            'str': 'anyString',
            'int': 100,
            'none': None
        }

        serialized = mj.serialize(validation_dict)
        deserialzed = mj.deserialize(serialized)

        self.assertDictEqual(validation_dict, deserialzed)

    def test_serialze_list(self):

        mj = MagicJson()

        validation_list = [
            date(2000,1,1),
            datetime(2010,11,12,13,14,15),
            time(20,21,22)
        ]

        serialized = mj.serialize(validation_list)
        deserialzed = mj.deserialize(serialized)

        self.assertListEqual(validation_list, deserialzed)