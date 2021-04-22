from django.shortcuts import render

def homepage(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits':num_visits
    }
    return render(request, 'website/index.html', context=context)

def lansupport(request):
    context = 0
    return render(request, 'website/lansupport.html', context={})
