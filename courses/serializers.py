from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.db.models import Avg

from .models import (
    Cource,
    Review,
)


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        extra_kwargs = {
            "email": {"write_only": True}
        }
        fields = '__all__'

    def validate_rating(self, value):
        if value in range(1,6):
            return value

        raise ValidationError("Rating must be an integer between 1 and 6")

        

class CourceSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)

    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Cource
        fields = '__all__'

    def get_average_rating(self,obj):
        average = obj.reviews.aggregate(Avg('rating')).get('rating__avg')

        if average is None:
            return 0
        
        return round(average*2) / 2
    










