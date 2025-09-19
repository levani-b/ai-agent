import os
from config import MAX_CHARS
from google.genai import types

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



schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file inside the working directory, with output truncated if it exceeds the maximum allowed length.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to read, from the working directory."
            ),
        },
        required=["file_path"]
    ),
)