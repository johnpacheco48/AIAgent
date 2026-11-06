import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    # Validator
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False: raise IndexError(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if os.path.isfile(target_dir) is False: raise TypeError(f'Error: "{file_path}" does not exist or is not a regular file')
        if file_path.endswith('.py') is False: raise TypeError(f'Error: "{file_path}" is not a Python file')

        # Subprocess
        command = ["python", os.path.abspath(target_dir)]
        if args: command.extend(args)
        process = subprocess.run(command, cwd=working_dir_abs, stdout=True, stderr=True, text=True, timeout=30, check=False)


        #Subprocess output
        process_output = ''
        if process.returncode != 0: process_output += f'Process exited with code {process.returncode}\n'
        if process.stderr == None and process.stdout == None: process_output += 'No output produced'
        else:
            process_output += f'STDOUT: {process.stdout}'
            process_output += f'STDERR: {process.stderr}'
        return process_output
    except Exception as e:
        print(e)

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Excecute Python files with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to the Python file, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",

                    },
                "description": "List of arguments to pass to the function (default value is None)"
                },
            },
        },
    },
}
