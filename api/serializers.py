from .models import User, Address, Geo, Company, Todos, Photo, Album, Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get("userId", instance.userId)
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.body = validated_data.get("body", instance.body)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        postId = validated_data.pop("postId", None)
        comment = Comment.objects.create(postId=postId, **validated_data)

        return comment


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ["userId", "id", "title", "completed"]


class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ["lat", "lng"]


class AddressSerializer(serializers.ModelSerializer):

    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ["street", "suite", "city", "zipcode", "geo"]


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name", "catchPhrase", "bs"]


class UserSerializer(serializers.ModelSerializer):

    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "email",
            "address",
            "phone",
            "website",
            "company",
        ]

    def create(self, validated_data):
        new_company = validated_data.pop("company", None)

        address = validated_data.pop("address", None)

        if address is not None:
            geo = address.pop("geo", None)
            new_adr = Address.objects.create(**address)
            if geo is not None:
                geol = Geo.objects.create(address=new_adr, **geo)

        if new_company is not None:
            company = Company.objects.create(**new_company)

        user = User.objects.create(address=new_adr, company=company, **validated_data)

        return user
