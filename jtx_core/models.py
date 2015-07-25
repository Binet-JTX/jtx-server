import datetime

from django.db import models
from django.utils import timezone

from rest_framework import serializers, viewsets



class TagKey(models.Model):
    """
    Key name for tag
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TagKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = TagKey
        

class TagKeyViewSet(viewsets.ModelViewSet):
    queryset = TagKey.objects.all()
    serializer_class = TagKeySerializer


class Tag(models.Model):
    class Meta:
        unique_together = ('key', 'value')

    key = models.ForeignKey(TagKey)
    value = models.CharField(max_length=254)

    def __str__(self):
        return '%s : %s' % (self.key.name, self.value)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

    _type = serializers.CharField(source = 'key.name', read_only=True)
    key = serializers.PrimaryKeyRelatedField(queryset=TagKey.objects.all(), write_only=True)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

