from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

# can also specify 'PUT' and 'POST'
@api_view(['GET'])
def get_route(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    # safe means we can use more than just python dictionary in the Json response
    return Response(routes)

@api_view(['GET'])
def get_rooms(request):
    rooms = Room.objects.all()
    # many means are there going to be more than one object to serialize
    serializers = RoomSerializer(rooms, many=True)
    return Response(serializers.data)

# if you wanted a user to be able to create a room from their own service
@api_view(['GET'])
def get_room(request, pk):
    room = Room.objects.get(id=pk)
    # many means are there going to be more than one object to serialize
    serializers = RoomSerializer(room, many=False)
    return Response(serializers.data)
