from magicjson.abstract import TypeSerializer

from typing import AnyStr
from datetime import date, datetime, time


class DateTimeSerializer(TypeSerializer):
    ID = 'dt'
    def serialize(obj: date | datetime | time) -> str:
        return obj.isoformat()

    def deserialize(str: AnyStr) -> date | datetime:
        if 'T' in str:
            return datetime.fromisoformat(str)
        if ':' in str:
            return time.fromisoformat(str)
        return date.fromisoformat(str)

