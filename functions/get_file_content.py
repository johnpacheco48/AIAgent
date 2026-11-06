import os


def get_file_content(working_directory:str, file_path: str) -> str:
    #Validator
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False: raise IndexError(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if os.path.isfile(target_dir) == False: raise TypeError(f'Error: File not found or is not a regular file: "{file_path}"')
    except (IndexError, TypeError) as e:
        print(e)
    # File Reader
    try:
        with open(target_dir) as file:
            contents = file.read(10_000)
            if file.read(1): contents += f'[...File "{file_path}" truncated at 10,000 characters]'
        return contents
    except Exception:
        f'Error: Unable to open or read "{file_path}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns the content of a specified file, truncating any file more than 10_000 characters long",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Directory path to the specified file, relative to the working directory",
                },
            },
        },
    },
}
