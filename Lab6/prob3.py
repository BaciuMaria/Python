import sys
import os

if len(sys.argv) != 2:
    print("Incorrect number of arguments!")
else:
    directory = sys.argv[1]
    size = 0

    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The given directory '{directory}' does not exist.")

        for path, directories, files in os.walk(directory):
            for file in files:
                size += os.path.getsize(os.path.join(path, file))

        print(f'The total size of all files in {directory}: {size} bytes')

    except FileNotFoundError:
        print(f'Error: Directory {directory} was not found.')
    except PermissionError:
        print(f'Error: Permission error for {directory}.')
    except Exception as e:
        print(f'Error: {e}')