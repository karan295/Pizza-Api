__author__ = 'Karan Dey'
from rest_framework import routers
from pizza_app import views
router=routers.DefaultRouter()
#create,delete
router.register(r'PizzaView',views.PizzaView,basename='PizzaView'),
#update
router.register(r'UpdatePizzaView',views.PizzaUpdateView,basename='UpdatePizzaView'),
#List filter
router.register(r'ListFilterPizzaView',views.PizzaListFilterView,basename='ListFilterPizzaView')
#list reterive

router.register(r'ListPizzaView',views.PizzaListView,basename='ListPizzaView')



urlpatterns = router.urls