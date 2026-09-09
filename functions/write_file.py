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

schema_write_file = {
	"type": "function",
	"function": {
		"name": "write_file",
		"description": "Writes content to a file relative to the working directory, creating or overwriting the file",
		"parameters": {
			"type": "object",
			"properties": {
				"file_path":{
					"type": "string",
					"description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
				},
			"content":{
					"type":"string",
					"description":"The content that wll be written to the file"
				}
			},
		"required": ["file_path","content"]
	},
    },
}
