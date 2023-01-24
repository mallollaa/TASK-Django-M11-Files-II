from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from islands import models


def get_islands(request: HttpRequest) -> HttpResponse:
    islands: list[models.Island] = list(models.Island.objects.all(),request.FILES)

    context = {
        "islands": islands,
    }

    return render(request, "island_list.html", context)

def create_island(request):
    island = island 
