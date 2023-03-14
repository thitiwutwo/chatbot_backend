from django.shortcuts import render
from django.http import JsonResponse

#hash password
from django.contrib.auth.hashers import make_password, check_password

#django rest framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework  import status

#import from app
from .models import *
from .serializers import *

# Create your views here.
data = {
    'message': 'Hello',
}

@api_view(['GET'])
def Home(request):
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def all_users(request):
    try:
        all_users = Users.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
#POST Data
@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        request.data['password'] = make_password(request.data['password'])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
# ใช้ Method PUT เพื่อส่งค่าไป Update ข้อมูล
@api_view(['PUT'])
def update_user(request, TID):
    user = Users.objects.get(id = TID)
    if request.method == 'PUT':
        data = {}
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status'] = 'updated'
            return Response(data = data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# ใช้ Method DELETE ในการลบข้อมูล ตาม id ที่ส่งมา
@api_view(['PUT'])
def delete_user(request,TID):
    user = Users.objects.get(id=TID)

    if request.method == 'PUT':
        user.is_deleted = True
        serializer = UserSerializer(user, data=user)
        if serializer.is_valid():
            data ['status'] = 'deleted'
            statuscode = status.HTTP_200_OK
        else:
            data['status'] = 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST
        return Response(data=data, status=statuscode)
    
@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        # parser_classes = (MultiPartParser, FormParser)
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_files(request):
    if request.method == 'GET':
        all_files = Files.objects.all()
        serializer = FileSerializer(all_files, many=True)
        for files in serializer.data:
            image_url = request.scheme + '://' + request.get_host() + files["file"]
            files["file"] = image_url
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_all_files(request):
    if request.method == 'GET':
        all_files = Files.objects.all()
        serializer = FileSerializer(all_files, many=True)
        for files in serializer.data:
            image_url = request.scheme + '://' + request.get_host() + files["file"]
            files["file"] = image_url
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def get_file(request, INTENT):

    if request.method == 'GET':
        try:
            file = Files.objects.get(intent=INTENT)
        except Files.DoesNotExist:
            return JsonResponse({'message': 'File not found'}, status=404)
        serializer = FileSerializer(file)
        response = serializer.data
        image_url = request.scheme + '://' + request.get_host() + response["file"]
        response["file"] = image_url
        return Response(response, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def Login(request):
#     if request.method == 'POST':
#         user = Users.objects.get(email = request.data['email'])
#         serializer = UserSerializer(user)
#         if user and check_password(request.data['password'], user.password):
#             return Response({"is_login": True}, status=status.HTTP_200_OK)
#         else:
#             return Response({"message": "user not found"}, status=status.HTTP_400_BAD_REQUEST)
#     if not serializer.is_valid():
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


