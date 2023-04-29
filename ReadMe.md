# File Management CLI using Python

This is a simple command-line interface (CLI) tool to perform basic file management operations using Python. The tool allows you to perform various file operations such as creating, deleting, renaming, and copying files and directories.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/file-manager.git
```

2. Navigate to the project directory:

```
cd file-manager
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Run the tool:

```
python file_manager.py
```

## Usage

Here's a brief explanation of what each command and subcommand will do:

**create file <path>**: creates a new file at the specified path.

**create directory <path>**: creates a new directory at the specified path.

**delete file <path>
delete directory <path> -r
rename <path> <newname>
copy <path> <destination>**: deletes the file at the specified path.

**delete file <path>
delete directory <path> -r
rename <path> <newname>
copy <path> <destination>**: deletes the directory and its contents recursively.

**delete file <path>
delete directory <path> -r
rename <path> <newname>
copy <path> <destination>**: renames the file or directory at the specified path to the new name.

**delete file <path>
delete directory <path> -r
rename <path> <newname>
copy <path> <destination>**: copies the file or directory at the specified path to the destination directory. If the source path is a directory, the contents of the directory will be copied recursively.

The program will output a message indicating whether the file management task was completed successfully.

## Contributing

If you find any issues or have ideas for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the GNU License - see the LICENSE.txt file for details.
