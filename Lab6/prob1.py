import sys
import os

if len(sys.argv) !=3 :
    print("Incorrect number of arguments!")
else:
    directory = sys.argv[1]
    extension = sys.argv[2]

    try:

        if not os.path.isdir(directory):
            raise FileNotFoundError(f'The given directory {directory} does not exist.')

        for file in os.listdir(directory):
            file_name, file_extension= os.path.splitext(file)
            if os.path.isfile(os.path.join(directory,file)) and file_extension == extension :
                try:
                    content = open(os.path.join(directory, file), 'r')
                    for line in content:
                        print(line.strip())
                    content.close()
                except Exception as e:
                    print(f'Error reading file {file}: {e}')
    except Exception as e:
        print(f'Error: {e}')