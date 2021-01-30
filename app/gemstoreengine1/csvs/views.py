from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
import csv
from sales.models import Sale
# Create your views here.

def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i==0:
                    pass
                else:
                    customer = row[0]
                    item = row[1]
                    total = row[2]
                    quantity = row[3]
                    date = row[4]
                    Sale.objects.update_or_create(
                        customer = customer,
                        item = item,
                        total = total,
                        quantity = quantity,
                        date = date,
                    )
            obj.activated = True
            obj.save()
    return render(request, 'csvs/upload.html', {'form': form})