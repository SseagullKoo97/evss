from django.shortcuts import render
from django.template.defaultfilters import random

from User_Homepage import models
from django.utils import timezone
from django.http import JsonResponse
from .models import Vehicle
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import uuid
import random
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def rent_page(request):
    stations = models.Station.objects.all()

    station_vehicles = {}
    for station in stations:
        # 查询每个站点的车辆，2个scooter和2个bike
        vehicles = models.Vehicle.objects.filter(current_location=station, vehicle_status='available')[:4]
        station_vehicles[station] = vehicles

    vehicle_pricing=models.VehiclePricing.objects.all()

    context = {
        'stations': stations,
        'station_vehicles': station_vehicles,
        'vehicle_pricing': vehicle_pricing
    }
    return render(request, 'Rentpage.html', context)

def time_page(request):
    current_time = timezone.now()  # 获取当前时间
    return render(request, 'time.html', {'current_time': current_time})


def rent_vehicle(request, vehicle_id):
    if request.method == 'POST':
        # 获取车辆并更新状态
        vehicle = get_object_or_404(Vehicle, vehicle_id=vehicle_id)
        vehicle.vehicle_status = 'in_use'
        vehicle.save()

        return JsonResponse({'status': 'success', 'message': 'Vehicle rented successfully.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)


def drop_vehicle(request, vehicle_id):
    if request.method == 'POST':
        # 获取车辆对象
        vehicle = get_object_or_404(Vehicle, pk=vehicle_id)

        # 更新车辆状态为 available
        vehicle.vehicle_status = 'available'
        vehicle.save()

        # 返回成功的 JSON 响应
        return JsonResponse({
            'status': 'success',
            'message': 'Vehicle dropped successfully!',
            'vehicle': {
                'vehicle_id': vehicle.vehicle_id,
                'vehicle_type': vehicle.vehicle_type,
                'battery_percentage': vehicle.battery_percentage,
                'vehicle_status': vehicle.vehicle_status
            }
        })

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method.'
    }, status=400)



#@login_required
#@csrf_exempt
def create_rental(request):
    print("is in -------------------")
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Request data:", data)
            vehicle_id = data.get('vehicle_id')
            print("Vehicle ID:", vehicle_id)
            customer_id = request.session.get('customer_id')
            customer = get_object_or_404(models.Customer, customer_id=customer_id)
            print("Customer ID:", customer_id)

            # 获取车辆对象和当前用户的起始站点信息
            vehicle = models.Vehicle.objects.get(vehicle_id=vehicle_id)
            print("Vehicle found:", vehicle)

            start_station = models.Station.objects.get(station_id=vehicle.current_location_id)  # 假设车辆的 current_location 表示起始站点
            print("Start station ID:", start_station.station_id)
            # rental_id = uuid.uuid4().int  #超范围
            while True:
                rental_id = random.randint(1, 10000)  # 生成1到10000之间的随机数
                if not models.Rental.objects.filter(rental_id=rental_id).exists():
                    break
            print("Rental ID:", rental_id)

            # 创建新的 Rental 记录
            rental = models.Rental.objects.create(
                rental_id=rental_id,
                customer_id=customer,
                vehicle_id=vehicle,
                start_time=timezone.now(),
                start_station_id=start_station,
                rental_status='active'
            )
            print("Rental created:", rental)

            return JsonResponse({'status': 'success', 'message': 'Rental created successfully!', 'rental_id': rental.rental_id})

        except Vehicle.DoesNotExist:
            print("Vehicle not found for vehicle_id:", vehicle_id)
            return JsonResponse({'status': 'error', 'message': 'Vehicle not found.'}, status=404)
        except Exception as e:
            print("Error occurred:", str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)
