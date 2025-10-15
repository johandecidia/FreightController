import mimetypes
import os

def detect_file_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if not mime_type:
        return "unknown"
    if "pdf" in mime_type:
        return "pdf"
    elif "csv" in mime_type:
        return "csv"
    elif "excel" in mime_type or file_path.endswith(('.xls', '.xlsx')):
        return "xls"
    return "unknown"
