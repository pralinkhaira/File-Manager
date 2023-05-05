# File Management CLI

This is a command-line interface (CLI) application for performing file management tasks such as creating, deleting, renaming, and copying files and directories. It is built using Python's built-in `os` module for file management tasks, and `argparse` for parsing command-line arguments.

## Getting Started

1. Clone this repository: `git clone https://github.com/BitH0xker/File-Manager.git`
3. Run the CLI application: `python File_Manager.py [command] [path] [options]`

## Usage

The CLI application supports the following commands:

### Create

Create a new file or directory.

```
python File_Manager.py create [type] [path]
```

- `type` (required): The type of file to create. Valid values are `file` and `directory`.
- `path` (required): The path to the file or directory to create.

### Delete

Delete a file or directory.

```
python File_Manager.py delete [path] [--recursive]
```

- `path` (required): The path to the file or directory to delete.
- `--recursive` (optional): Delete directory and its contents recursively.

### Rename

Rename a file or directory.

```
python File_Manager.py rename [path] [newname]
```

- `path` (required): The path to the file or directory to rename.
- `newname` (required): The new name for the file or directory.

### Copy

Copy a file or directory.

```
python File_Manager.py copy [path] [destination]
```

- `path` (required): The path to the file or directory to copy.
- `destination` (required): The destination directory to copy the file or directory to.

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.
