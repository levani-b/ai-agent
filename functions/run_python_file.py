import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    target_file_absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_absolute_path = os.path.abspath(working_directory)

    if not target_file_absolute_path.startswith(working_dir_absolute_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file_absolute_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ['python', target_file_absolute_path,*args],
            timeout=30,
            capture_output=True,
            text=True,
            cwd=working_dir_absolute_path
        )

        output_parts = []

        if result.stdout.strip():
            output_parts.append(f"STDOUT:\n{result.stdout.strip()}")

        if result.stderr.strip():
            output_parts.append(f"STDERR:\n{result.stderr.strip()}")

        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not output_parts:
            return "No output produced."

        return "\n".join(output_parts)

    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out after 30 seconds'
    except Exception as e:
        return f"Error: executing Python file: {e}"
