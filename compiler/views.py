

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from compiler.forms import CodeSubmissionForm
from django.conf import settings
import os
import uuid
import subprocess
from pathlib import Path
import sys

def submit(request):
    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            print(submission.language)
            print(submission.code)
            output = run_code(
                submission.language, submission.code, submission.input_data
            )
            submission.output_data = output
            submission.save()
            return render(request, "result.html", {"submission": submission})
    else:
        form = CodeSubmissionForm()
    return render(request, "index1.html", {"form": form})

def run_code(language, code, input_data):
    app_path = Path(settings.BASE_DIR) / 'compiler'
    directories = ["codes", "inputs", "outputs"]

    for directory in directories:
        dir_path = app_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    codes_dir = app_path / "codes"
    inputs_dir = app_path / "inputs"
    outputs_dir = app_path / "outputs"

    unique = str(uuid.uuid4())

    code_file_name = f"{unique}.{language}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = inputs_dir / input_file_name
    output_file_path = outputs_dir / output_file_name

    with open(code_file_path, "w") as code_file:
        code_file.write(code)
    
    formatted_input_data = input_data.strip().replace('\r\n', '\n').replace('\r', '\n')

    with open(input_file_path, "w") as input_file:
        input_file.write(formatted_input_data)

    with open(output_file_path, "w") as output_file:
        pass  # This will create an empty file

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    subprocess.run(
                        [str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                    )
    
    elif language == "c":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["gcc", str(code_file_path), "-o", str(executable_path)]
        )
        if compile_result.returncode == 0:
            with open(input_file_path, "r") as input_file:
                with open(output_file_path, "w") as output_file:
                    subprocess.run(
                        [sys.executable, str(executable_path)],
                        stdin=input_file,
                        stdout=output_file,
                    )
   
    elif language == "py":
        # Code for executing Python script
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    [sys.executable, str(code_file_path)],  # Using sys.executable
                    stdin=input_file,
                    stdout=output_file,
                )
    
    # Read the output from the output file
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()
        
    # Debugging: Print contents for checking
    print(f"Input File Content: {formatted_input_data}")
    print(f"Output File Content: {output_data}")
    return output_data.strip()

