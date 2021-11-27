from rest_framework import generics
from .models import Post
from .serializers import PostSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView





class Createuser(APIView):#2

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostList(generics.ListCreateAPIView): 
    permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer