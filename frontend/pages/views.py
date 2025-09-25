import requests
from django.shortcuts import render

API_BASE = "http://backend:8000/api"

def courses_list(request):
    response = requests.get(f"{API_BASE}/courses/")
    courses = response.json()
    return render(request, "courses_list.html", {"courses": courses})

def disciplines_list(request):
    response = requests.get(f"{API_BASE}/disciplines/")
    disciplines = response.json()
    return render(request, "disciplines_list.html", {"disciplines": disciplines})
