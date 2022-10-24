from rest_framework import serializers

from api.models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ["name",
                "size",
                "friendliness",
                "trainability",
                "shedding_amount",
                "exercise_needs",
                ]

class DogSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(many=False, queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = ["name",
                "age",
                "breed",
                "gender",
                "color",
                "favorite_food",
                "favorite_toy"]
