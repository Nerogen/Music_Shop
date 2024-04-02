from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProductCard
from .serializer import ProductCardSerializer


class ProductCardView(APIView):
    def get(self, request):
        output = [
            {
                "image": output.image,
                "item_name": output.item_name,
                "cost": output.cost,
                "info": output.info
            } for output in ProductCard.objects.all()
        ]

        return Response(output)

    def post(self, request):
        serializer = ProductCardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
