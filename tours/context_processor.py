from tours import data


def code_base(request):

    return {
        "title": data.title,
        "departures": data.departures,
    }
