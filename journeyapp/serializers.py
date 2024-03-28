from rest_framework import serializers
from . import models


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ["id","title","genre","image","description","date_finished","favourite","opinion"]
    date_finished = serializers.DateTimeField(format='%b %d, %Y', required=False)
    favourite = serializers.BooleanField(required=False)
    opinion = serializers.CharField(required=False)
    
    
class WishListSerializer(serializers.ModelSerializer ):
    class Meta:
        model = models.WishList
        fields = "__all__"
    date_wished = serializers.DateTimeField(format='%b %d, %Y', required=False)