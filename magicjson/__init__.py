from dataclasses import dataclass, field
from json import dumps, loads
from typing import Any

from magicjson.abstract import TypeSerializer, SerializerMap
from magicjson.constants import SERIALIZER_MAP
from magicjson.helper import validate_serializer_map, transpose_serializer_map

def serialzer_default() -> SERIALIZER_MAP:
    return SERIALIZER_MAP

@dataclass(slots=True)
class MagicJson:
    serializer_map: SerializerMap = field(default_factory=serialzer_default)
    reverse_map: dict[str, TypeSerializer] = field(init=False)
    marker_entry = '['
    marker_exit = ']'
    separator = '|'

    def _serialize(self, obj: Any):
        """JSON serializer for objects not serializable by default json code"""
        try:
            serializer = self.serializer_map.get(type(obj))
            return f'{self.marker_entry}{serializer.ID}{self.marker_exit}{self.separator}{serializer.serialize(obj)}'
        except KeyError:
            pass
        raise TypeError ("Type %s not serializable" % type(obj))

    def __post_init__(self):
        self.reverse_map = transpose_serializer_map(self.serializer_map)

    def serialize(self, obj: Any):
        return dumps(
				obj, default=self._serialize
			)

    def _deserialze(self, any: Any):
        if isinstance(any, str):
            if self.separator in any:
                _ = any.split(self.separator)
                marker, content = _[0], self.separator.join(_[1:])
                if marker.startswith(self.marker_entry) and marker.endswith(self.marker_exit):
                    marker = marker.replace(self.marker_entry,'').replace(self.marker_exit,'')
                    return self.reverse_map[marker].deserialize(content)
                else:
                    return any
            return any
        if isinstance(any, list):
            return [self._deserialze(item) for item in any]
        if isinstance(any, dict):
            return {k:self._deserialze(v) for k,v in any.items()}


    def deserialize(self, any: Any):
        _json = loads(any)
        return self._deserialze(_json)
