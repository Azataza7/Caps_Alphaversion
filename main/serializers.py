from rest_framework import serializers
from .models import Item, Brand, SizeVariant
from rest_framework.exceptions import ValidationError


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    size = SizeSerializer()

    class Meta:
        model = Item
        fields = '__all__'


class ItemValidateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    brand_id = serializers.IntegerField()
    size_id = serializers.IntegerField()
    count = serializers.IntegerField()

    class Meta:
        model = Item
        fields = 'id title description brand_id size_id count'.split()

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def validate_brand_id(self, brand_id):
        try:
            Brand.objects.get(brand_id=brand_id)
        except:
            return brand_id
        raise ValidationError('This brand does not exists')
