from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        readonly_fields = ["id", "created_at", "modified_at"]
