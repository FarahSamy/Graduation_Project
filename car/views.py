from django.shortcuts import render

# Create your views here.
def test(request):
    context = {
        'name':'farah'
    }
    return render(request, 'test.html', context)