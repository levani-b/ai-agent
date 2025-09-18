import os

def get_files_info(working_directory, directory="."):
    relative_path = os.path.join(working_directory, directory)
    target_absolute_path = os.path.abspath(relative_path)
    absolute_working_dir = os.path.abspath(working_directory)

    if not target_absolute_path.startswith(absolute_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    directory_content = os.listdir(target_absolute_path)

    try:
        files_info = []
        for content in directory_content:
            content_path = os.path.join(target_absolute_path, content)
            is_dir = os.path.isdir(content_path)
            size = os.path.getsize(content_path)
            files_info.append(f'- {content}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

