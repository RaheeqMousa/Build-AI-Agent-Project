import os

def write_file(working_directory:str, file_path:str, content:str) -> str:
	try:
		working_dir_abs= os.path.abspath(working_directory)

		target_path= os.path.normpath(
			os.path.join(working_dir_abs, file_path)
		)

		is_valid_path= os.path.commonpath(
			[working_dir_abs, target_path]) == working_dir_abs

		if not is_valid_path:
			return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
		if os.path.isdir(target_path):
			return f'Error: Cannot write to "{file_path}" as it is a directory'

		with open(target_path, "w") as f:
			f.write(content)

		return f'Successfully wrote to "{target_path}" ({len(content)} characters written)'
	except Exception as ex:
		return f"Error: {ex}"
