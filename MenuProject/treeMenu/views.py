from django.shortcuts import render


def base(request):
    return render(request, 'treeMenu/base.html')
