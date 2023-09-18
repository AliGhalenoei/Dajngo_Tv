from rest_framework import serializers
from accounts.models import *
from content.models import *
# Serializers App Accounts 

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

class SingupSerializer(serializers.Serializer):
    phone = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate_phone(self,value):
        if User.objects.filter(phone = value).exists():
            raise serializers.ValidationError('Phone is alredy...')
        return value
    
    # def validate_phone(self,value):
    #     if len(value) > 11:
    #         raise serializers.ValidationError('Number Phone invalid...')
    #     return value
    
    def validate_email(self,value):
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError('email is alredy...')
        return value
    
    def validate(self,value):
        #value = self.validated_data
        if value['password'] and value['password2'] and value['password'] != value['password2']:
            raise serializers.ValidationError('Passwords is not Match')
        return value

    # def create(self, validated_data):
    #     del validated_data['password2']
    #     return User.objects.cretae_user(**validated_data)


# Serializers App Content 

class CategorySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields=('name','slug','img','category')

    def get_category(self,obj):
        result = obj.cate_movie.all()
        return MovieSerializer(instance = result , many = True).data
    
class MovieSerializer(serializers.ModelSerializer):
    #category = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields=('__all__')   

class SeryalMovieSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SeryalMovie
        fields=('__all__')

class LikeMovieSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = LikeMovie
        fields=('__all__')

class LikeSeryalMovieSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = LikeSeryal
        fields=('__all__')

class CommentMovieSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields=('__all__')

class CommentSeryalMovieSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    movie = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = CommentSeryal
        fields=('__all__')





        

