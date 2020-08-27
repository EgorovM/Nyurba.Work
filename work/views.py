from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers

from .models import Order


def index(request):
    if request.method == "POST":
        order = Order.fill_by_post(request.POST)
        if "image" in request.FILES:
            order.image = request.FILES['image']

        order.save()

    return render(request, 'index.html')


@csrf_exempt
def add_order(request):
    if request.method == "POST":
        order = Order.fill_by_post(request.POST)
        order.save()

    return JsonResponse({"error": "ok"})


def get_orders(request):
    def media_url(image_name):
        return request._current_scheme_host + "/media/" + image_name

    orders = eval(serializers.serialize("json", Order.objects.all()[::-1]))

    for ind, order in enumerate(orders):
        orders[ind]["fields"]["image"] = "http://" + request.META['HTTP_HOST'] + "/media/" + orders[ind]["fields"]["image"]

    return JsonResponse({"results" : orders})


@csrf_exempt
def view_order(request):
    if request.method == "POST":
        id = request.POST.get('id')
        order = Order.objects.get(id=id)
        order.viewsCount += 1
        order.save()

    return JsonResponse({"status" : "ok"})
