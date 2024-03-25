from rest_framework import serializers

class Web3eventSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 100)
    image = serializers.CharField(max_length = 100)
    source_url = serializers.CharField(max_length = 100)
    event_url = serializers.CharField(max_length = 100)
    summary = serializers.CharField(max_length = 300)
    description = serializers.CharField()
    title = serializers.CharField(max_length = 100)