from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Estudiante, Pago
import json

@csrf_exempt
def nuevo_pago(request):
    if request.method == 'POST':
        try:
            # Parsear el cuerpo de la solicitud como JSON
            data = json.loads(request.body.decode('utf-8'))
            
            # Obtener los datos del pago desde el JSON
            estudiante_id = data.get('estudiante_id')
            valor = data.get('valor')
            
            # Validar que los campos requeridos están presentes
            if estudiante_id is None or valor is None:
                return JsonResponse({'error': 'Faltan datos requeridos (estudiante_id, valor).'}, status=400)
            
            # Validar que el valor sea un número positivo
            if not isinstance(valor, int) or valor <= 0:
                return JsonResponse({'error': 'El valor del pago debe ser un número entero positivo.'}, status=400)
            
            # Obtener el estudiante de la base de datos
            estudiante = get_object_or_404(Estudiante, id=estudiante_id)
            
            # Crear y guardar el nuevo pago
            pago = Pago(
                estudiante=estudiante,
                valor=valor
                # fecha_pago se establecerá automáticamente
            )
            pago.save()
            
            # Devolver una respuesta exitosa
            return JsonResponse({'mensaje': 'pago guardado exitosamente', 'pago_id': pago.pk}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido.'}, status=400)
        except Exception as e:
            # Manejar otras excepciones generales
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método HTTP no permitido. Solo se permite POST.'}, status=405)
    
def home(request):
    return render(request, 'home.html')