from rest_framework import serializers
from . import models


class WordSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk', 'word', 'translation']