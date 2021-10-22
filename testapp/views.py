from django.http import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import server_error
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import *
import json
from rest_framework.response import Response

# Create your views here.
class TypeApiView(generics.ListCreateAPIView):
    queryset=pizza_type.objects.all()
    serializer_class=PizzaTypeSerializer
    
class SizeApiView(generics.ListCreateAPIView):
    queryset=pizza_size.objects.all()
    serializer_class=PizzaSizeSeriaizer

class ToppingsApiView(generics.ListCreateAPIView):
    queryset=pizza_size.objects.all()
    serializer_class=PizzaSizeSeriaizer


class PizzaCrud(APIView):
    def post(self,request):
        post_type=request.path
        allowed_types=['regular','square']
        sizes=list(x['size'] for x in pizza_size.objects.all().values('size'))
        # toppings=list(x['toppings'] for x in pizza_toppings.objects.all().values('toppings'))
        type_obj=pizza_type.objects.all()
        size_obj=pizza_size.objects.all()
        toppings_obj=pizza_toppings.objects.all()

        data=json.loads(self.request.body)
        if data.get('pizza_type') not in allowed_types:
                return Response({'error':'please select between regular and square types'})
        if data.get('pizza_size') not in sizes:
           return Response({'error':f'please select from these sizes{sizes}'})
        if 'createsquare' in post_type:
            data['pizza_type']=pizza_type.objects.get(type=data.get('pizza_type')).id
        elif 'createregular' in post_type:
            data['pizza_type']=pizza_type.objects.get(type=data.get('pizza_type')).id
        
        
        data['pizza_size']=size_obj.get(size=data.get('pizza_size')).id
        toppingss=data.get('pizza_toppings').split(',')
        X=list(x['id'] for x in toppings_obj.filter(toppings__in=toppingss).values('id'))
        if len(toppingss)!=len(toppings_obj.filter(toppings__in=toppingss).values('id')):
            return Response('please enter only selected toppings from menu')

        data['pizza_toppings']=toppingss
        Serializer=PizzaOrdersSerializer(data=data)
        if Serializer.is_valid():
           Serializer.save()
           return Response({'status':"sucess"})
        else:
           return Response(Serializer.errors)   

class GetAllPizza(generics.RetrieveDestroyAPIView):
    def get(self,request):
        if len(request.GET)==0:
            a=pizza_orders.objects.all()
        elif request.GET.get('type')!=None:
            a=pizza_orders.objects.filter(pizza_type=self.getTypeID(request.GET.get('type')))
        elif request.GET.get('size')!=None:
            a=pizza_orders.objects.filter(pizza_size=self.getSizeId(request.GET.get('size')))
        elif request.GET.get('type')!=None and request.GET.get('size')!=None:
            a=pizza_orders.objects.filter(pizza_size=self.getSizeId(request.GET.get('size')),pizza_type=self.getTypeID(request.GET.get('type')))
                 
        else:
            a=pizza_orders.objects.all()
        data={}
        for obj in a:
            row={}
            row['pizza type']=pizza_type.objects.get(type=obj.pizza_type).__dict__.get('type')
            row['pizza_size']=pizza_size.objects.get(size=obj.pizza_size).__dict__.get('size')
            row['pizza_toppings']=obj.pizza_toppings
            data[f'{obj.order_id}']=row
    
        return Response(data)
    


    def getTypeID(self,type):
        try:
            obj= pizza_type.objects.filter(type=type)
            return obj[0].id
        except:
            return Response({'status':'type not found'})
            
    def getSizeId(self,size):
        try:
            obj= pizza_size.objects.filter(size=size)
            return obj[0].id
        except:
            return Response({'status':'size not found'})
    def delete(self, request,id):
        try:
            obj= pizza_orders.objects.get(order_id=id)
            obj.delete()
            return Response({'status':'deleted'})   
        except:
            return Response({'status':'record not found'})
               
    
        






        
