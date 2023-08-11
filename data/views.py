from django.shortcuts import render
from http.client import HTTPResponse
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from treemenu.models import Scheme
from .resources import SchemeResource
 
# Create your views here.
 
def import_excel(request):
     
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        dbframe = pd.read_excel(filename)        
        for dbframe in dbframe.itertuples():
            parent_scheme = Scheme.objects.filter(number = dbframe.parent)
            if parent_scheme:
                obj = Scheme.objects.create(name=dbframe.name, number=dbframe.number,
                                            parent=parent_scheme[0], chapter = dbframe.chapter, 
                                            chineese_name = dbframe.chineese_name, quantity = dbframe.quantity
                                            )
            else:
                 # first create parent
                 parent_obj = obj = Scheme.objects.create(name='неизвестная схема с номером '+ dbframe.parent, number=dbframe.parent, 
                                                        chapter = dbframe.chapter, chineese_name = dbframe.chineese_name, 
                                                        quantity = dbframe.quantity) 
                 # then create child 
                 obj = Scheme.objects.create(name=dbframe.name, number=dbframe.number, parent = parent_obj,
                                            chapter = dbframe.chapter, chineese_name = dbframe.chineese_name, 
                                            quantity = dbframe.quantity)          
                 parent_obj.save() 
            obj.save()
        return render(request, 'data/Import_excel_db.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'data/Import_excel_db.html',{})
