import requests
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse
from rest_framework.parsers import JSONParser
from album.models import Album


class AlbumListView(View):
    template_name = "index.html"

    def get_context_data(self, sorting_parameter="", **kwargs):
        context = {}
        context["datas"] = self.get_queryset(sorting_parameter)
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        sorting_parameter = f"?sorting={self.request.POST.get('sorting')}"
        context = self.get_context_data(sorting_parameter)
        return render(request, self.template_name, context)

    def get_queryset(self, sorting_parameter=""):
        url = self.request.build_absolute_uri(
            reverse("albums-list") + f"{sorting_parameter}"
        )
        request = requests.get(url)
        return request.json()
