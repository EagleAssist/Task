from django.shortcuts import render

from rest_framework import generics


from .models import Companies
from .serializers import CompaniesSerialize

class ModelList(generics.ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerialize
def model_list(request):
    data = Companiesl.objects.all()
    return render(request, 'templates/list.html', {'data': data})