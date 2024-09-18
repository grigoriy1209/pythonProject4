from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    year = serializers.IntegerField()
    create_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
