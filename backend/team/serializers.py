from core import models

from rest_framework import serializers


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for the team object."""

    class Meta:
        model = models.Team
        fields = '__all__'

    # def create(self, validated_data):
    #     """Create and return a user with encrypted password."""
    #     return get_user_model().objects.create_user(**validated_data)

    # def update(self, instance, validated_data):
    #     """Update and return user."""
    #     password = validated_data.pop('password', None)
    #     user = super().update(instance, validated_data)

    #     if password:
    #         user.set_password(password)
    #         user.save()

    #     return user
    