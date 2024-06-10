from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import PermissionDenied

class HomeView(View):
    def get(self, request, *args, **kwargs):
        group = request.user.groups.first()
        if not group:
            raise PermissionDenied
        return render(request, 'index.html')
