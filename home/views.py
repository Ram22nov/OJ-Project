from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

#added
from home.models import Problem
from compiler.forms import CodeSubmissionForm
from compiler.views import run_code



def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problem_list.html', {'problems': problems})

# views.py in your home app
from django.shortcuts import render, get_object_or_404
from home.models import Problem
from compiler.forms import CodeSubmissionForm
from compiler.views import run_code

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    output = None
    code = ""
    language = "py"
    input_data = problem.input_data
    expected_output = problem.expected_output
    result = None
    results = []

    if request.method == 'POST':
        action = request.POST.get('action')
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            language = form.cleaned_data['language']
            user_input_data = form.cleaned_data['input_data']
            if action == 'run':
                output = run_code(language, code, user_input_data)
            elif action == 'submit':
                # Split the input and expected output into lines
                input_cases = input_data.split('\n')
                expected_outputs = expected_output.split('\n')
                all_passed = True

                for i, input_case in enumerate(input_cases):
                    if input_case.strip() == "":
                        continue
                    output = run_code(language, code, input_case)
                    expected = expected_outputs[i].strip()
                    actual = output.strip()
                    if actual == expected:
                        results.append(("Passed", input_case, actual, expected))
                    else:
                        results.append(("Failed", input_case, actual, expected))
                        all_passed = False

                result = "All test cases passed" if all_passed else "Some test cases failed"

    return render(request, 'problem_detail.html', {
        'problem': problem,
        'code': code,
        'language': language,
        'output': output,
        'result': result,
        'results': results,
    })

#added



#def practice(request):
 #  return render(request,'practice.html')

def contest(request):
    return render(request,'contest.html')
    #return HttpResponse("this is contest page")
     



def profile(request):
    return HttpResponse("this is profile page")
    

# Create your views here.
def index(request):
    return render(request,'index.html')

