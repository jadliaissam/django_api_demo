from random import randint

from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Product
from app.serializers import ProductSerializer
from faker import Faker


def home(request):
    return HttpResponse("Hello Wrold from Demo API")


def seed_data(request, count):
    fake = Faker()
    for i in range(count):
        Product.objects.create(
            title=fake.sentence(nb_words=randint(3, 7)),
            code=fake.isbn10(),
            image=f"https://picsum.photos/id/{randint(100, 300)}/200/300",
            description=fake.paragraph(nb_sentences=randint(2, 8)),
            price=randint(250, 20000)
        )
    return HttpResponse(f"Seed Successuful for {count} product(s)")


def clean(request):
    Product.objects.all().delete()
    return HttpResponse(f"Deleted All Products Successfully !!")


class CustomTokenAuthentication(TokenAuthentication):
    keyword = "Token"


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
