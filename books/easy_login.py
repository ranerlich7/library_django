from django.shortcuts import render, redirect

def elogin(request):
    if request.POST:
        return redirect('books:books')
    else:
        context = {}
        return render(request,'elogin.html',context=context)