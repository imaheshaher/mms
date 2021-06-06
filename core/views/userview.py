from django.http.response import Http404
from rest_framework.views import APIView
from core.models import User

from rest_framework.response import Response
from core.utils import MyAPIView
from core.utils.viewsets import MyModelViewSet,MyCreateRetrieveUpdateViewSet
from core.serializers import UserSerialilzer, userserializer
from rest_framework.viewsets import ModelViewSet

class UserViewSet(MyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerialilzer



class UserApiView(MyAPIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def get(self,request,pk=None):
        if pk is not None:
            user = self.get_object(pk)
            serializer = UserSerialilzer(user)

        else:
            user=User.objects.all()
            serializer = UserSerialilzer(user,many=True)

        # user=User.objects.all()
        return Response(serializer.data)

    def post(self,request):
        serializer=UserSerialilzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":serializer.errors})

    def put(self,request,pk):
        user=self.get_object(pk)
        serializer = UserSerialilzer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":serializer.errors})
   


