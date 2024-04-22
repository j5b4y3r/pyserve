from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse
import os
from . import tests

def get_data(requested_path=os.path.expanduser('~'), file=None):
    fobject = []
    if os.path.exists(requested_path):
        tests.list_files_and_folders(requested_path, fobject)
    return fobject

def home(request):
    return render(request, 'home.html', {'data': get_data()})

def download_file(request, file_path):
    # Construct the absolute file path
    absolute_file_path = os.path.abspath(file_path)

    # Check if the file exists
    if os.path.isfile(absolute_file_path):
        try:
            # Create a FileResponse object and return it
            response = FileResponse(open(absolute_file_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(absolute_file_path)}"'
            return response
        except Exception as e:
            # Handle any exceptions that may occur during file download
            return HttpResponse("Error downloading file: " + str(e), status=500)
    else:
        # Return a response indicating that the file was not found
        return HttpResponse("File not found", status=404)

def play_file(request, file_path):
    # Construct the absolute file path
    absolute_file_path = os.path.abspath(file_path)

    # Check if the file exists
    if os.path.isfile(absolute_file_path):
        try:
            # Create a FileResponse object to stream the file content
            response = FileResponse(open(absolute_file_path, 'rb'))
            response['Content-Disposition'] = f'inline; filename="{os.path.basename(absolute_file_path)}"'
            response['Content-Type'] = 'video/mp4'
            return response
        except Exception as e:
            # Handle any exceptions that may occur during file streaming
            return HttpResponse("Error streaming file: " + str(e), status=500)
    else:
        # Return a response indicating that the file was not found
        return HttpResponse("File not found", status=404)

def send_ff(request, path):
    check = path.split("/")
    if check[0] == "download":
        return download_file(request, path[9:])
    elif check[0] == "play":
        return play_file(request, path[9:])
    else:
        return JsonResponse(get_data(path), safe=False)


