import os

def get_files_info(working_directory, directory = None):
    if directory is None:
        full_path = os.path.abspath(working_directory)
    else:
        full_path = os.path.abspath(os.path.join(working_directory, directory))
    
    working_directory_abs = os.path.abspath(working_directory)

    if not full_path.startswith(working_directory_abs):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    

    try:
        contents = os.listdir(full_path)
        
        result_lines = []
        for item in contents:
            item_path = os.path.join(full_path, item)
            try:
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                result_lines.append(f" - {item}: file_size={file_size} bytes, is_dir={is_dir}")
            except OSError as e:
                result_lines.append(f" - {item}: Error getting file info - {str(e)}")
        
        return "\n".join(result_lines)
    
    except OSError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"