# These views render the database as JSON
from django.shortcuts import render
from django.core import serializers
from application.serializers import SpaceSerializer
from application.models import Space
from django.http import HttpResponse,JsonResponse
from django.db.models import Q

def all_innovation_spaces(request):
    spaces = Space.objects.all()
    serializer = SpaceSerializer(spaces, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_space(request, id):
    space = Space.objects.get(id=id)
    serializer = SpaceSerializer(space)
    return JsonResponse(serializer.data)

def filter_spaces(request):
    filter_terms = request.GET
    spaces = Space.objects.all()

    if 'name' in filter_terms:
        spaces = spaces.filter(name__icontains=filter_terms['name'])

    if 'all_text' in filter_terms:
        spaces = spaces.filter(Q(name__icontains=filter_terms['all_text']) |
                               Q(description__icontains=filter_terms['all_text']) |
                               Q(short_description__icontains=filter_terms['all_text']))

    if 'country' in filter_terms:
        countries = filter_terms['country'].split(",")
        spaces = spaces.filter(country__in=countries)

    if 'operational_status' in filter_terms:
        if filter_terms['operational_status'] == "null":
            spaces = spaces.filter(operational_status__isnull=True)
        else:
            spaces = spaces.filter(operational_status__iexact=\
                                filter_terms['operational_status'])

    if 'not_closed' in filter_terms:
        spaces = spaces.exclude(operational_status__iexact="Closed")

    if 'network_affiliation' in filter_terms:
        spaces = spaces.filter(network_affiliation__name=filter_terms['network_affiliation'])


    if 'fields' in filter_terms:
        fields = filter_terms['fields'].split(",")
    else:
        fields = None

    serializer = SpaceSerializer(spaces, fields=fields, many=True)

    return JsonResponse(serializer.data, safe=False)

# We're not going to allow for programmatic creation/editing/deleting for fear
# that there will be spambots that take advantage of those features and ruin
# the database
