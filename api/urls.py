"""api routes"""

from django.urls import path, include
from api.views.stories import stories
from api.views.topstories_id import topstories

urlpatterns = [
    path('stories/<int:index>/<int:num>', stories),
    path('topstories/', topstories)
]
