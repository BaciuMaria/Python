import sys
import os

if len(sys.argv) != 2:
    print("Incorrect number of arguments!")
else:
    directory = sys.argv[1]

    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f'The given directory {directory} does not exist.')

        files = os.listdir(directory)

        if not files:
            raise Exception(f"Empty directory.")

        extensions = {}
        for file in files:
            if os.path.isfile(os.path.join(directory, file)):
                file_name, file_extension = os.path.splitext(file)
                extensions[file_extension] = extensions.get(file_extension, 0) + 1

        for extension, count in extensions.items():
            print(f'{extension} : {count}')

    except Exception as e:
        print(f'Error: {e}')