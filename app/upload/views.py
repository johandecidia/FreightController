from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UploadedFile
from .utils import detect_file_type

class FileUploadView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "upload/upload.html")

    def post(self, request):
        file_obj = request.FILES.get("file")
        if not file_obj:
            return JsonResponse({"error": "No file provided"}, status=400)

        # TODO: Replace this with actual client logic
        client_id = request.user.id  # temporary placeholder

        uploaded = UploadedFile.objects.create(
            user=request.user,
            client_id=client_id,
            file=file_obj
        )

        file_type = detect_file_type(uploaded.file.path)
        uploaded.file_type = file_type
        uploaded.save()

        return JsonResponse({
            "message": "File uploaded successfully",
            "file_name": uploaded.file.name,
            "file_type": uploaded.file_type,
        })
