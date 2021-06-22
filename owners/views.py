
import json

from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dog 

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        print(data["name"]) 

        owners = Owner.objects.create(
            name=data['name'], 
            email=data['email'], 
            age=data['age']
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        # print(type(data['name']))
        dog = Dog.objects.create(
            name=data['name'],
            age=data['age'],
            owner_id=Owner.objects.get(name=data['owner_name'])
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status = 201)