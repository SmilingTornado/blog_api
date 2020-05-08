from blogapi.models import Card
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogapi.serializers import CardSerializer

@api_view(['GET', 'PUT'])
def card_list(request):

    if request.method == 'GET':
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def card_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        card = Card.objects.get(pk=pk)
    except Card.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CardSerializer(card)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)