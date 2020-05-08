from django.contrib.auth.models import User, Group
from blogapi.models import Card
from rest_framework import serializers

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['pk','name','status','category','content','author']