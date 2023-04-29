import os
import argparse

# Define the command-line arguments
parser = argparse.ArgumentParser(description='File Management CLI')
parser.add_argument('command', choices=['create', 'delete', 'rename', 'copy'], help='The command to execute')
parser.add_argument('path', help='The path to the file or directory')

# Define the subcommands for each file management task
subparsers = parser.add_subparsers(dest='subcommand', title='Subcommands')

# Create subcommand
create_parser = subparsers.add_parser('create', help='Create a new file or directory')
create_parser.add_argument('type', choices=['file', 'directory'], help='The type of file to create')

# Delete subcommand
delete_parser = subparsers.add_parser('delete', help='Delete a file or directory')
delete_parser.add_argument('--recursive', '-r', action='store_true', help='Delete directory and its contents recursively')

# Rename subcommand
rename_parser = subparsers.add_parser('rename', help='Rename a file or directory')
rename_parser.add_argument('newname', help='The new name for the file or directory')

# Copy subcommand
copy_parser = subparsers.add_parser('copy', help='Copy a file or directory')
copy_parser.add_argument('destination', help='The destination directory to copy the file or directory to')

# Parse the command-line arguments
args = parser.parse_args()

# Execute the appropriate file management task based on the command and subcommand
if args.command == 'create':
    if args.type == 'file':
        open(args.path, 'a').close()
    elif args.type == 'directory':
        os.makedirs(args.path)
    print(f'{args.path} created successfully.')

elif args.command == 'delete':
    if args.subcommand == 'file':
        os.remove(args.path)
    elif args.subcommand == 'directory':
        if args.recursive:
            os.removedirs(args.path)
        else:
            os.rmdir(args.path)
    print(f'{args.path} deleted successfully.')

elif args.command == 'rename':
    new_path = os.path.join(os.path.dirname(args.path), args.newname)
    os.rename(args.path, new_path)
    print(f'{args.path} renamed to {new_path} successfully.')

elif args.command == 'copy':
    if os.path.isdir(args.path):
        os.makedirs(args.destination, exist_ok=True)
        for item in os.listdir(args.path):
            source_path = os.path.join(args.path, item)
            destination_path = os.path.join(args.destination, item)
            if os.path.isdir(source_path):
                os.makedirs(destination_path, exist_ok=True)
                shutil.copytree(source_path, destination_path)
            else:
                shutil.copy2(source_path, destination_path)
    else:
        shutil.copy2(args.path, args.destination)
    print(f'{args.path} copied to {args.destination} successfully.')
