import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    target_file_absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_absolute_path = os.path.abspath(working_directory)


    if not target_file_absolute_path.startswith(working_dir_absolute_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file_absolute_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file_absolute_path, 'r', encoding="utf-8") as f:
            file_content_string = f.read(MAX_CHARS + 1)
    except Exception as e:
        return f"Error: {str(e)}"
    
    if len(file_content_string) > MAX_CHARS:
        file_content_string = (
            file_content_string[:MAX_CHARS]
            + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        )     

    return file_content_string


