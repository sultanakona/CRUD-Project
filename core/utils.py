from rest_framework.response import Response

def api_response(data=None, message="OK", status_code=200, success=True):
    return Response(
        {
            "statusCode": status_code,
            "success": success,
            "message": message,
            "data": data,
        },
        status=status_code,
    )
