from .serializer import date, datetime, time, DateTimeSerializer

SERIALIZER_MAP = {
    date: DateTimeSerializer,
    datetime: DateTimeSerializer,
    time: DateTimeSerializer,
}