from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializers


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderListView(ListAPIView):
    serializer_class = OrderSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_class = OrderSerializers
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def update(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            serializer = self.get_serializer(order, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def destroy(self, request, *args, **kwargs):
        try:
            order = self.get_object()
            self.perform_destroy(order)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)