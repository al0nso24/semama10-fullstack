#academia/views.py
from django.http import HttpResponse, JsonResponse

def saludo(request, nombre):
 return HttpResponse(f'Hola, {nombre}.')

def sumar(request):
 a = float(request.GET.get('a', 0))
 b = float(request.GET.get('b', 0))
 return JsonResponse({'resultado': a + b})