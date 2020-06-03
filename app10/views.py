from django.shortcuts import render

def show_index(request):
    d1={
        "Emp1":{"IDno":"e1122","name":"Ravi","desg":"software developer","salary":50000.00},
        "Emp2": {"IDno": "e2244", "name": "Ramu", "desg": "software developer", "salary":80000.00}
        }
    return render(request,"index.html",{"data":d1})
