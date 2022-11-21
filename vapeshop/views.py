from django.shortcuts import render


def error_404(request, exception):
    """"
    Handles HTTP 404 errors
    """

    return render(request, 'errors/404.html')


def error_500(request,):
    """"
    Handles HTTP 500 errors
    """
    return render(request, 'errors/500.html')
