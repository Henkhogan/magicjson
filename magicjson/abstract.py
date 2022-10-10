from __future__ import annotations


from abc import ABC, abstractstaticmethod
from typing import Any, AnyStr


class TypeSerializer(ABC):
    ID: str
    @abstractstaticmethod
    def serialize(obj: Any) -> str | int | float:
        pass
    
    @abstractstaticmethod
    def deserialize(str: AnyStr) -> Any:
        pass
    
SerializerMap = dict[type, TypeSerializer]
