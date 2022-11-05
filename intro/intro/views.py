from django.shortcuts import HttpResponse


def hello(request):
    return HttpResponse("Hello, world!")


def welcome(request):
    # res = "<!DOCTYPE html><html><head><title>Przywitanie</title></head><body><h2>Witaj, Jurek!</h2></body></html>"
    res = """
        <!DOCTYPE html>
            <html>
                <head>
                    <title>Przywitanie</title>
                </head>
                <body>
                    <h2>Witaj, Jurek!</h2>
                </body>
            </html>
    """
    return HttpResponse(res)
