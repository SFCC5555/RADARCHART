from binascii import a2b_hex
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
import plotly.express as px
import pandas as pd
from fpdf import FPDF
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
    df = pd.DataFrame(dict(
        r=valores,
        theta=['pregunta1','pregunta2','pregunta3',
            'pregunta4', 'pregunta5']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.show()
    return render(request, "CHART/resultados.html", {
        "valores":valores
    })

