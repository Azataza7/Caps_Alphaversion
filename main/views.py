from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def test_view(request):
    dict_ = {
        'text': 'Hello world',
        'int': 123
    }
    return Response(data=dict_)