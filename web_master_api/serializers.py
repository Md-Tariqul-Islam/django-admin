from rest_framework import serializers

from .models import MenuItem, WebsiteDetail


class WebsiteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteDetail
        fields = "__all__"

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"