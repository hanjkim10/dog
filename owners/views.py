
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
        
    def get(self, rquest):
    
        owners = Owner.objects.all()
        result_owner = []
       
        for owner in owners:
            dog_list = []
            dogs = Dog.objects.all()

            for dog in dogs:
                my_dict = {
                    'name' : dog.name,
                    'age': dog.age
                }
                dog_list.append(my_dict)
            owner_dict = {
            'name' : owner.name,
            'age' : owner.age,
            'email' : owner.email,
            'dog_list' : dog_list
            }
            result_owner.append(owner_dict)
        return JsonResponse({"result": result_owner}, status = 200)
    
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
    
    def get(self, request):
        dog_list = []
        dogs = Dog.objects.all()
        for dog in dogs:
            my_dict = {
                'owner' : dog.owner_id.name,
                'name' : dog.name,
                'age' : dog.age
            }
            dog_list.append(my_dict)
        return JsonResponse({"result" : dog_list}, status = 200)



