from django.urls import path
from . import views

app_name="CHART"
urlpatterns = [
    path("",views.index, name="index"),
    path("pregunta1", views.pregunta1, name="pregunta1"),
    path("pregunta2", views.pregunta2, name="pregunta2"),
    path("pregunta3", views.pregunta3, name="pregunta3"),
    path("pregunta4", views.pregunta4, name="pregunta4"),
    path("pregunta5", views.pregunta5, name="pregunta5"),
    path("enviar", views.enviar, name="enviar"),
    path("resultados", views.resultados, name="resultados"),

]