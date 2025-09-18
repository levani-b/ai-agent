import os

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

