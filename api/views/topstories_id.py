import json
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache


def topstories(request):
    """return all the id's topstories"""

    if cache.get("tps"):
        recipe = cache.get("tps")
        return JsonResponse(recipe, safe=False)

    else:
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
        stories_list = requests.get(url).json()
        cache.set("tps", stories_list, timeout=10)
        return JsonResponse(stories_list, safe=False)
