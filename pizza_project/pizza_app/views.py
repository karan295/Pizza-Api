__author__ = 'Karan Dey'
  
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from pizza_app.serializers import PizzaSerializer,PizzaListSerializer
from django.contrib.auth.models import User
from .models import Pizza,PizzaToppings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

#create,delete
class PizzaView(viewsets.ViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def list(self,request):
        queryset=Pizza.objects.all()
        serializers=PizzaListSerializer(queryset,many=True)
        return Response(serializers.data)

    def create(self,request):
        try:
            user=User.objects.get(username=request.user)
        except:
            return Response("User not found")

        serializers=PizzaSerializer(data=request.data)
        if(serializers.is_valid()):
            Pizza_type=serializers.data['Pizza_type']
            Pizza_Size=serializers.data['Pizza_Size']
            pizza=Pizza.objects.create(Pizza_type=Pizza_type,Pizza_Size=Pizza_Size,createdBy=user)
            for i in serializers.data['Pizza_toppings']:
                try:
                    toppings=PizzaToppings.objects.get(Name=i['Name'])
                    pizza.Pizza_toppings.add(toppings)
                except:
                    toppings=PizzaToppings.objects.create(Name=i['Name'])
                    pizza.Pizza_toppings.add(toppings)

            return Response(serializers.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)


    def destroy(self,request,pk):
        try:
            pizza=Pizza.objects.get(id=pk)
            pizza.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response("Pizza with id {} not found".format(pk),status=status.HTTP_400_BAD_REQUEST)





class PizzaListView(viewsets.ViewSet):
      def list(self,request):
        queryset=Pizza.objects.all()
        serializers=PizzaListSerializer(queryset,many=True)
        return Response(serializers.data)
      def retrieve(self,request,pk):
          try:
              data=Pizza.objects.get(id=pk)
              serializers=PizzaListSerializer(data)
              return Response(serializers.data)

          except:
              return Response("Pizza with id {} not found".format(pk),status=status.HTTP_400_BAD_REQUEST)







#update
class PizzaUpdateView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def update(self,request,pk):
        try:
            user=User.objects.get(username=request.user)
        except:
            return Response("User not found")
        try:
            pizza=Pizza.objects.get(id=pk)
            serializers=PizzaSerializer(data=request.data)
            if(serializers.is_valid()):
                pizza.Pizza_Size=request.data.get('Pizza_Size',pizza.Pizza_Size)

                pizza.Pizza_type=request.data.get('Pizza_type',pizza.Pizza_type)
                l=[]
                for i in pizza.Pizza_toppings.all():
                    l.append(i.id)

                for j in serializers.data['Pizza_toppings']:
                    try:
                        c=PizzaToppings.objects.get(Name=j['Name'])
                        if(c.id in l):
                            l.remove(c.id)

                        else:
                            pizza.Pizza_toppings.add(c)
                    except:

                        c=PizzaToppings.objects.create(Name=j['Name'])
                        pizza.Pizza_toppings.add(c)
                if(len(l)!=0):
                    for i in l:
                        s=PizzaToppings.objects.get(id=i)
                        pizza.Pizza_toppings.remove(s)
                pizza.UpdateBy=user
                pizza.save()

                return Response(serializers.data,status=status.HTTP_200_OK)
            else:
                return Response(serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response("Pizza with id {} not found".format(pk),status=status.HTTP_400_BAD_REQUEST)



# List filter
class PizzaListFilterView(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields=("Pizza_type","Pizza_Size")
