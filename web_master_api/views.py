from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MenuItem, WebsiteDetail
from .serializers import MenuItemSerializer, WebsiteDetailSerializer


class WebsiteDetailListApiView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            web_details = WebsiteDetail.objects.all()
            web_details_data = WebsiteDetailSerializer(web_details, many=True).data if web_details else {}

            menu_items = MenuItem.objects.all()
            menu_items_data = MenuItemSerializer(menu_items, many=True).data if menu_items else {}

            response_dict = {
                'web_details': web_details_data,
                'menu_items': menu_items_data
            }

            return Response(response_dict, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)