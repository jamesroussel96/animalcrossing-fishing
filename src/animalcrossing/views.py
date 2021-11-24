from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Fish


# Create your views here.
# request handler


def read_calc(request):
    return render(request, 'index.html')


def fish_search_view(request, *args, **kwargs):
    query_dict = request.GET #dictionary
    print(query_dict)
    query = query_dict.get("Season")
    fish_obj_season = None
    if query is not None:
        fish_obj_season = Fish.objects.get(season=query) 
    context = {
        "object": fish_obj_season
    }
    return render(request, "fish.html", context=context)

