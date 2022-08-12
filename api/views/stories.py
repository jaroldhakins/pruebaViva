import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache



def stories(request, index, num):
    """shows the details of the num stories since index"""

    if cache.get("stories"):
        recipe = cache.get("stories")
        return JsonResponse(recipe, safe=False)

    url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    stories_list = requests.get(url).json()
    first = 'https://hacker-news.firebaseio.com/v0/item/'
    second = '.json?print=pretty'
    my_list = []

    for i in stories_list[index:index+num]:
        url2 = first + str(i) + second
        data = requests.get(url2).json()
        story = {"titulo": data.get("title"), "ID": data.get("id")}
        my_list.append(story)
    
    cache.set("stories", my_list, timeout=10)
    return JsonResponse(my_list, safe=False)
