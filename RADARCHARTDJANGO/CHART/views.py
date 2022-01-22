from django import forms
from django.http import HttpResponse
from django.shortcuts import render

valores = []

class NuevoValor(forms.Form):
    valor = forms.IntegerField(label="Valor",min_value=1, max_value=100)

# Create your views here.
def index(request):
    return render(request, "CHART/index.html")

def pregunta1(request):
    if request.method == "POST":
        form = NuevoValor(request.POST)
        if form.is_valid():
            valor = form.cleaned_data["valor"]
            valores.append(valor)
        else:
            return render(request, "CHART/pregunta1.html", {
                "form": form
            })
    return render(request, "CHART/pregunta1.html", {
        "form": NuevoValor()
    })

def pregunta2(request):
    if request.method == "POST":
        form = NuevoValor(request.POST)
        if form.is_valid():
            valor = form.cleaned_data["valor"]
            valores.append(valor)
        else:
            return render(request, "CHART/pregunta2.html", {
                "form": form
            })
    return render(request, "CHART/pregunta2.html", {
        "form": NuevoValor()
    })

def pregunta3(request):
    if request.method == "POST":
        form = NuevoValor(request.POST)
        if form.is_valid():
            valor = form.cleaned_data["valor"]
            valores.append(valor)
        else:
            return render(request, "CHART/pregunta3.html", {
                "form": form
            })
    return render(request, "CHART/pregunta3.html", {
        "form": NuevoValor()
    })

def pregunta4(request):
    if request.method == "POST":
        form = NuevoValor(request.POST)
        if form.is_valid():
            valor = form.cleaned_data["valor"]
            valores.append(valor)
        else:
            return render(request, "CHART/pregunta4.html", {
                "form": form
            })
    return render(request, "CHART/pregunta4.html", {
        "form": NuevoValor()
    })

def pregunta5(request):
    if request.method == "POST":
        form = NuevoValor(request.POST)
        if form.is_valid():
            valor = form.cleaned_data["valor"]
            valores.append(valor)
        else:
            return render(request, "CHART/pregunta5.html", {
                "form": form
            })
    return render(request, "CHART/pregunta5.html", {
        "form": NuevoValor()
    })

def enviar(request):
    if request.method == "POST":
        form = NuevoValor(request.POST)
        if form.is_valid():
            valor = form.cleaned_data["valor"]
            valores.append(valor)
        else:
            return render(request, "CHART/enviar.html", {
                "form": form
            })
    return render(request, "CHART/enviar.html", {
        "form": NuevoValor()
    })

def resultados(request):
    return render(request, "CHART/resultados.html", {
        "valores":valores
    })