from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """"serializers serializes a name field for api view"""
    name = serializers.CharField(max_length = 10)
    place = serializers.CharField(max_length = 5)
