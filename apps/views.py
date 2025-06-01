from django.http import JsonResponse
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.models import Category, Book
from apps.serializers import CategoryModelSerializer, BookModelSerializer, UserModelSerializer


@extend_schema(tags=["Hello_API"])
@api_view(['GET'])
def hello_world_api_view(request):
    return JsonResponse({'message': 'Hello Bewrlius Wolmberg !'})


@extend_schema(tags=["Create_Books"], request=BookModelSerializer, responses=BookModelSerializer, )
@api_view(['POST'])
def book_create_api_view(request):
    obj = Book.objects.create(**request.data)
    serialize = BookModelSerializer(instance=obj)
    return JsonResponse(serialize.data)


@extend_schema(tags=["Update_book"], request=BookModelSerializer, responses=BookModelSerializer)
@api_view(['PUT'])
def book_update_api_view(request, pk):
    data = request.data
    obj = Book.objects.filter(pk=pk)
    obj.update(**data)
    json_data = BookModelSerializer(instance=obj, many=True)
    return JsonResponse({"Status": 200, "message": "Muvaffaqiyatli o'zgartirildi ", "data": json_data.data})


@extend_schema(tags=["Create_category"], request=CategoryModelSerializer, responses=CategoryModelSerializer)
@api_view(['POST'])
def category_create_api_view(request):
    seralizer = CategoryModelSerializer(data=request.data)
    if request.method == 'POST':
        seralizer.is_valid(raise_exception=True)
        seralizer.save()
    return JsonResponse(seralizer.data)


@extend_schema(tags=["Delete_category"])
@api_view(['DELETE'])
def category_delete_api_view(request, pk):
    Category.objects.get(pk=pk).delete()
    return JsonResponse({"Status": 200, "message": "Muvaffaqiyatli o'chrildi "})


@extend_schema(tags=["Update_category"], request=CategoryModelSerializer, responses=CategoryModelSerializer)
@api_view(['PUT'])
def category_update_api_view(request, pk):
    data = request.data
    objects = Category.objects.filter(pk=pk)
    objects.update(**data)
    json_data = CategoryModelSerializer(instance=objects, many=True)
    return JsonResponse({"Status": 200, "message": "Muvaffaqiyatli o'zgartirildi ", "data": json_data.data})


@extend_schema(tags=["List_category"])
@api_view(['GET'])
def category_list_api_view(request):
    objects = Category.objects.all()
    json_data = CategoryModelSerializer(instance=objects,many=True)
    return Response(json_data.data)


@extend_schema(tags=['Add number API '],parameters=[
    OpenApiParameter(
        name='son1',
        description='Birinchi sonni kiriting :',
        required=True,
        type=int),
    OpenApiParameter(
        name='son2',
        description='Ikkinchi sonni kiriting :',
        required=True,
        type=int),
])

@api_view(['GET'])
def add_api_view(request):
    son1 = int(request.GET.get('son1'))
    son2 = int(request.GET.get('son2'))
    return JsonResponse({'Natija': son1+son2})

@extend_schema(tags=['User Model'], request=UserModelSerializer, responses=UserModelSerializer)
@api_view(['POST'])
def register_api_view(request):
    data = request.data
    serializer = UserModelSerializer(data=data)
    if serializer.is_valid():
        obj = serializer.save()
    return JsonResponse(UserModelSerializer(instance=obj).data)


