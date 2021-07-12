from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from tours import data
import random


def main_view(request):
    random_tours = dict(random.sample(data.tours.items(), 6))

    context = {
        "random_tours": random_tours,
        "subtitle": data.subtitle,
        "description": data.description,
    }
    return render(request, 'tours/index.html', context=context)


def departure_view(request, departure):

    dep = data.departures[departure]

    departure_tours = {tour_id: tour for (tour_id, tour) in data.tours.items() if tour["departure"] == departure}

    vals = {
        "max_value": max([tour.get("price") for tour in departure_tours.values()]),
        "min_value": min([tour.get("price") for tour in departure_tours.values()]),
    }
    nights = {
        "max_value": max([tour.get("nights") for tour in departure_tours.values()]),
        "min_value": min([tour.get("nights") for tour in departure_tours.values()]),
    }

    context = {
        "dep_tours": departure_tours,
        "departure": dep,
        "vals": vals,
        "nights": nights,
    }
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, tour_id):

    tour = data.tours[tour_id]
    departure = data.departures.get(tour["departure"])
    stars = range(int(tour["stars"]))

    context = {
        "tour": tour,
        "departure": departure,
        "stars": stars,
    }
    return render(request, 'tours/tour.html', context=context)


# обработка ошибок
def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найдет!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
