from rest_framework import serializers
from .models import Organisation, OrgGallery, Donation


class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model= Organisation
        fields='__all__'

class OrgGallerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model= OrgGallery
        fields='__all__'

class Donation(serializers.ModelSerializer):
    
    class Meta:
        model= Donation
        fields='__all__'