from django.shortcuts import render
from django.views.generic import View

import firebase_admin

from firebase_admin import credentials
from firebase_admin import db

# Create your views here.

class Objects(View):
    template_name = "index.html"

    cred = credentials.Certificate("./metroid-objects-firebase-adminsdk-80rnc-f20e398f9f.json")

    firebase_admin.initialize_app(cred, {'databaseURL': 'https://metroid-objects-default-rtdb.firebaseio.com/'})

    ref = db.reference('objects')

    datos = ref.get()

    def get(self, request):
        return render(request, self.template_name, {"objects": self.datos})