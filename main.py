import os
import json
import shutil

source_path = 'c:\wamp64\singlecoreb2b'
destination_path = r'c:\wamp64\blade\singlecoreb2b'
output_folder = 'c:\wamp64\output'
output_original = 'c:\wamp64\original'
json_path = 'file.json'

source_files = [os.path.join(dp1, f) for dp1, dn1, filenames in os.walk(source_path) for f in filenames]
destination_files = [os.path.join(dp2, f) for dp2, dn2, filenames in os.walk(destination_path) for f in filenames]

files = []
original_files = []

for file in source_files:
    search_file = file.replace(r'c:\wamp64\singlecoreb2b', r'c:\wamp64\blade\singlecoreb2b')
    if search_file not in destination_files:
        if search_file.find('node_modules') == -1:
            print(file)
            files.append(file)

    else:
        if os.path.getsize(file) != os.path.getsize(search_file):
            if file.find('node_modules') == -1:
                files.append(file)
                original_files.append(search_file)
                print(file)

for file in files:
    file_name = file.split('\\')[-1]
    file_path = '\\'.join(file.split('\\')[3:-1])
    output_file_path = os.path.join(r'c:\wamp64\output', file_path)
    print(output_file_path)
    os.makedirs(output_file_path, exist_ok=True)
    shutil.copyfile(file, os.path.join(output_file_path, file_name))

    print(f'Copied {file} > {os.path.join(output_file_path, file_name)}')

for original_file in original_files:
    file_name = original_file.split('\\')[-1]
    file_path = '\\'.join(original_file.split('\\')[4:-1])
    output_file_path = os.path.join(r'c:\wamp64\original', file_path)
    print(output_file_path)
    os.makedirs(output_file_path, exist_ok=True)
    shutil.copyfile(original_file, os.path.join(output_file_path, file_name))

    print(f'Copied {original_file} > {os.path.join(output_file_path, file_name)}')

# with open(json_path, 'w') as outfile:
#     json.dump(files, outfile, indent= 4)
