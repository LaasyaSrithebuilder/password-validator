
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import run_validators

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    errors = run_validators(password)
    if errors:
        return JsonResponse({"error": errors[0]}, status=400)

    return JsonResponse({"message": "Login successful"})
