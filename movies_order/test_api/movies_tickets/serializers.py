from rest_framework import serializers


class MovieBaseSerializer(serializers.Serializer):
    error_messages = {
        'required': 'missing_field',
        'invalid': 'invalid',
    }


class MovieDetailSerializer(serializers.Serializer):
    error_messages = {
        'required': 'missing_field',
        'invalid': 'invalid',
    }


class CinameSerializer(serializers.Serializer):
    error_messages = {
        'required': 'missing_field',
        'invalid': 'invalid',
    }

class SessionSerializer(serializers.Serializer):
    error_messages = {
        'required': 'missing_field',
        'invalid': 'invalid',
    }
