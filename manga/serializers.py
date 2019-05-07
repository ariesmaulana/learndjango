from rest_framework import serializers
from .models import Mangas

class MangasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mangas
        fields = ("title", "author")