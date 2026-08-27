from django.http import HttpResponse, JsonResponse

def inicio(request):
    return HttpResponse('Modulo de productos Activo!')

def acerca(request):
    return HttpResponse('API de ejemplo para la semana 3')

def api_productos(request):
    if request.method == 'GET':
        datos = [
            {'id':1, 'nombre':'Teclado'},
            {'id':2, 'nombre':'Mouse'},
        ]
        return JsonResponse(datos, safe=False)

    return JsonResponse(
        {'error':'Metodo no permitido'},
        status=405
    )


