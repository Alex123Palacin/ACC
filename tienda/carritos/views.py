from rest_framework import viewsets
from .models import Carrito
from .serializers import CarritoSerializer


class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
