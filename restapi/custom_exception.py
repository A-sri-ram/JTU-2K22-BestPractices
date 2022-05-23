from rest_framework.exceptions import APIException


class UnauthorizedUserException(APIException):
<<<<<<< Updated upstream
    status_code: int = 404
    default_detail: str = "Not Found"
    default_code: str = "Records unavailable"
=======
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Not Found"
    default_code = "Records unavailable"
>>>>>>> Stashed changes
