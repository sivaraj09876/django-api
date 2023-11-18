from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_api(request):
    if request.method=='GET':
        context={
            'api_status':True,
            'message':'Hello World!'
        }
        return Response(context,status=status.HTTP_200_OK)
    else:
        context={
            'api_status':False,
            'error':'only GET method allowed'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)