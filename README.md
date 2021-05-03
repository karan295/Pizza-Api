# Pizza-Api
In this pizza project i use 3 three api for different functionality
1:- "PizzaView": "http://127.0.0.1:8000/PizzaView/" in this api all the information about the pizza like pizza size, pizza toppings and pizza type
are list and we can also use post method for create pizza list for user.

database use : MongoDB
Also use serializer and restframework

2:- "ListFilterPizzaView": "http://127.0.0.1:8000/ListFilterPizzaView/" in this api all the information about the pizza are listed
and post,delete and filter method is also use here in which user can delete the list and also use filter method and user can also know the single list information using id.

3:- "ListPizzaView": "http://127.0.0.1:8000/ListPizzaView/" in this api all the information about the pizza which are listed are shown and also show information by id.

In this api user is allow to edit or delete any pizza from the database.

And api is also use to lists the information about all the stored pizza, the response of this should also contain the information about the toppings, size and type of Pizza.

And Api allows to filtering the list of pizza returned by the API based on Size & Type of Pizza.

step to run the projects:-
first run on shell after create project and app python manage.py makemigrtions,then run migrate for created database command then finally
write python manage.py runserver command for running localhost 127.0.0.1:8000

then click on three api





