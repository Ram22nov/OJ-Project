from django.shortcuts import render, HttpResponse, get_object_or_404

#added
from home.models import Problem
from compiler.forms import CodeSubmissionForm
from compiler.views import run_code


def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problem_list.html', {'problems': problems})

# views.py in your home app

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    output = None

    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            code = form.cleaned_data['code']
            input_data = form.cleaned_data['input_data']
            output = run_code(language, code, input_data)
            
    else:
        form = CodeSubmissionForm()

    return render(request, 'problem_detail.html', {
        'problem': problem,
        'form': form,
        'output': output,
    })
#added



#def practice(request):
 #  return render(request,'practice.html')

def contest(request):
    return render(request,'contest.html')
    #return HttpResponse("this is contest page")
     
def discuss(request):
    return render(request,'discuss.html')

def profile(request):
    return render(request,'profile.html')



# Create your views here.
def index(request):
    return render(request,'index.html')

