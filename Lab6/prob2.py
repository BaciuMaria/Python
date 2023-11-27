import sys
import os

if len(sys.argv) !=2 :
    print("Incorrect number of arguments!")
else:
    directory = sys.argv[1]

    try:

        if not os.path.isdir(directory):
            raise FileNotFoundError(f'The given directory {directory} does not exist.')

        index = 1
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory,file)):
                file_name, file_extension= os.path.splitext(file)
                try:
                    os.rename(old_file,new_file)
                    print(f'Succesfully renames {old_file} to {new_file}.')
                    index +=1

                except Exception as e:
                    print(f'Error renaming {old_file}: {e}')
    except Exception as e:
        print(f'Error: {e}')