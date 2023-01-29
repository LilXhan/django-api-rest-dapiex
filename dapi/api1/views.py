from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Country
from .serializers import CountrySerializer

@api_view(['GET', 'POST', 'PUT'])
def country(request):

    print(request)

    if request.method == 'GET':
        snippets = Country.objects.all()
        serialiazer = CountrySerializer(snippets, many=True)
        return Response(serialiazer.data)
        
    elif request.method == 'POST':

        print(request.data)

        serialiazer = CountrySerializer(data=request.data)

        if serialiazer.is_valid():
            serialiazer.save()
            return Response(serialiazer.data, status=status.HTTP_201_CREATED)

        return Response(serialiazer.errors, status=status.HTTP_400_BAD_REQUEST)