import json
from django.contrib.auth.models import Group

with open("out.json") as j:
    data = json.load(j)

for row in data:
    Group(id=1).records.create(name=row["Servicio"], value=float(row["Monto"]))
