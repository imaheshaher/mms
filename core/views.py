import json
from django.http.response import JsonResponse

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes,permission_classes,renderer_classes


from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import *
from .serializers import *
from django.contrib.auth import login,authenticate
# Create your views here.

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER
class RegisterApiview(APIView):
    permission_classes=(AllowAny,)
    def get(self,request):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class MenuViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



class FeedbackViewset(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class PresentViewset(viewsets.ModelViewSet):
    queryset = Present_Customer.objects.all()
    serializer_class = PresentSerializer

class FeedbackApiview(APIView):
    def get(self,request):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            menu=Menu.objects.get(id=1)
            serializer.save(feedback="this is feedback",menu=menu)
            return Response(serializer.data)
        return Response("data")




class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self,request):
        username=request.data["username"]
        password = request.data["password"]
        user = authenticate(username=username,password=password)
        if user is not None:
            
            try:
                payload = JWT_PAYLOAD_HANDLER(user)
                jwt_token = JWT_ENCODE_HANDLER(payload)
            except:
                return Response("error")
        else:
            return Response({
                "error":"User Not found"
            })
        return Response({
            'username':user.username,
            "token":jwt_token
        })



@csrf_exempt
@api_view(('GET',))

@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])

def check_login(request):
    print("login")
    try:
        # print(request.user.__dict__)
        a=request.user.username
        k=json.dumps(a)
        m=json.loads(k)
        return JsonResponse({"data:":m})
    except:
        return Response("not login")
