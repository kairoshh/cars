from django.urls import path

from mainapp.views import CarMarkView

from rest_framework.routers import DefaultRouter as DR

from mainapp.views import CarModelView

router = DR()

router.register('car_model', CarModelView)


urlpatterns = [
    path('create_cars/', CarMarkView.as_view()),
]

urlpatterns += router.urls