import os
from google.genai import types

def write_file(working_directory, file_path, content):
    target_file_absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_absolute_path = os.path.abspath(working_directory)

    if not target_file_absolute_path.startswith(working_dir_absolute_path):
        return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isdir(working_dir_absolute_path):
        return f'Error: Working directory not found: "{working_directory}"'
    
    if os.path.exists(target_file_absolute_path) and os.path.isdir(target_file_absolute_path):
        return f'Error: Path points to a directory: "{file_path}"'


    parent_dir = os.path.dirname(target_file_absolute_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    with open(target_file_absolute_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a file inside the working directory, creating parent directories if needed.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to write, from the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file."
            ),
        },
        required=["file_path", "content"]
    ),
)