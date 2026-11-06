import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:

        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        if os.path.isdir(target_dir) == False: raise TypeError(f"Error: {directory} is not a directory")
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir == False: raise IndexError(f'''Error: Cannot list "{directory}" as it is outside the permitted working directory''')
        if valid_target_dir == True:
            print(f'''Success: "{directory}" is within the working directory''')
            # i iterations are rerturning after one iteration, fix to have function return
            # all results in the directory
            directory_list: list[str] = []
            for i in os.listdir(target_dir):
                try:

                    file_path = os.path.join(target_dir, i)
                    file_name = i
                    file_size = os.path.getsize(file_path)
                    file_isdirectory = os.path.isdir(file_path)
                    directory_list.append(f"- {file_name}: file_size={file_size} bytes, is_dir={file_isdirectory}\n")

                except Exception:
                    print(f"Error: {i} is not a valid file or directory")
            #return f"- {file_name}: file_size={file_size} bytes, is_dir={file_isdirectory}"
            return "\n".join(directory_list)
    except (IndexError, TypeError) as e:
        return e


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
