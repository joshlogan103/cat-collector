from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cat, Feeding, Toy

class ToySerializer(serializers.ModelSerializer):
  class Meta:
    model = Toy
    fields = '__all__'
  
class CatSerializer(serializers.HyperlinkedModelSerializer):
  fed_for_today = serializers.SerializerMethodField()
  toys = ToySerializer(many=True, read_only=True)
  user = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = Cat
    fields = '__all__'
    extra_kwargs = {'url': {'view_name': 'cat-detail', 'lookup_field': 'id'}}

  def get_fed_for_today(self, obj):
    return obj.fed_for_today()
  
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only
    cats = CatSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'cats')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

class FeedingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feeding
    fields = '__all__'
    read_only_fields = ('cat',)