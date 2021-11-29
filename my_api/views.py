from django.db import connection
from rest_framework import generics
from .models import Post , Student , Teacher ,Mybook
from .serializers import PostSerializer , UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q


class PostDetail(generics.RetrieveUpdateDestroyAPIView):#waste


    # permission_classes = [IsAuthenticated] 
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Createuser(APIView):#2 #waste

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#####################################orm explore

        # Students =  Student.objects.all()
        # print(Students.query)#prints sql query 
        # print(connection.queries)#get the extra details than above ie  execution time 
        # Students =  Student.objects.filter(surname__startswith="j")
        #or
        # Students =  Student.objects.filter(surname__endswith="v") | Student.objects.filter(surname__endswith="j")
        # posts = Student.objects.filter(Q(surname__startswith='da') |  Q (surname__startswith='o'))
        #and
        # Students =  Student.objects.filter(surname__startswith="d") & Student.objects.filter(surname__startswith="d")#norml and
        # Students =  Student.objects.filter(surname__startswith="d") & Student.objects.exclude(surname__startswith="l")#and with exlude
        # posts = Student.objects.filter(Q(surname__startswith="d") &  Q (age="24"))
        #union used to combine 2 queries  eg 2 tables has same surename , have to combine into one query
        #if 2 tables has the same name , it filter only one and no duplicates
        #valuelist gives tup inside list
        #value gives as dictnary
        # posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))#keep in mind , it removes the duplicate
        #not (exclude)
        # Students =  Student.objects.exclude(age="24") &  Student.objects.exclude(age="26")#exclude not working with q so written as below
        # posts = Student.objects.exclude(age__in=["24",'28'])#q no
        #operations 
        #gt
        #gte
        # lt
        #lte
        # posts = Student.objects.exclude(age__gt="24")#q no       
        #excluding with ~q
        # posts = Student.objects.filter(~Q(age='26') & ~Q(surname__startswith="d"))#
        #quey filtering (usefull without using the serializer) can specify which dataa we need
        # posts = Student.objects.filter(classroom=1).only('firstname','age')
        #$$ using raw instead of filter we can get data using the Raw sql query
        #from django.db.models import Sum, Max, Min, Avg 
        #used for db total operation using aggregate
        # product = Mybook.objects.all().aggregate(newname=Sum("cost"))#we can override the na e also

#####################################orm explore
#problem solution arised at product cupboard , book


# 2.multi table inheritance eg:

        # product = Product.objects.all()
        # a =product[0] 
        # print(a.book.publisher)#how the data is accessed 
        # print(a.cupboard.shelves)#how the data is accessed 
        #main
        #for in the case of front end the product is iterated 
        # when iterating like this  product.book.publisher and product.cupboard.shelves more queries get executed inorder to reduce th query we use the 
        #select related , crates a sql join
        # product = Product.objects.all().select_related('book','cupboard')#here in curent case select related has min query
        # product = Product.objects.all().prefetch_related('book','cupboard')#both are situationally used 

# 2.multi table inheritance eg:  ends
       
############################################### search using posgres


class PostList(APIView):#soln 2

    def get(self, request):
        product = Mybook.objects.all().aggregate(newname=Sum("cost"))#we can override the na e also
   

        print("posts")
        print(product)
        print("posts")
        return Response("serializer.data", status=status.HTTP_201_CREATED)





