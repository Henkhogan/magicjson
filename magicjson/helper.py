from magicjson.abstract import TypeSerializer, SerializerMap

def transpose_serializer_map(serializer_map: SerializerMap):
    _out = {}
    for k,v in serializer_map.items():
        _out[v.ID] = v
    return _out

def validate_serializer_map(serializer_map: SerializerMap):
    raise NotImplementedError