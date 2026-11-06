import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    # Validator
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False: raise IndexError(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(target_dir) is True: raise TypeError(f'Error: Cannot write to "{file_path}" as it is a directory')

        os.makedirs(file_path, exist_ok=True)
        with open(target_dir, mode="w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except (IndexError, TypeError) as e:
        print(e)

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to the file specified by the file path. Overwrites content of the file if the file already exists, otherwise will make a new file at the specified file path",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to the specified file, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content that will be written to the specified file"
                }
            },
        },
    },
}
