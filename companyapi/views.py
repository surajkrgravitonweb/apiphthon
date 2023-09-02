from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page")
    friends=[
        'ankit',
        'ravi',
        'uttam'
    ]
    return JsonResponse(friends, safe=False)
    return HttpResponse("this is page")