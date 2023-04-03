import argparse
import os
import sys
import uuid

parser = argparse.ArgumentParser()
parser.add_argument('--folder', '-f', required=True, help='relative path to folder, where files are stored')
parser.add_argument('--rounds', '-r', required=True, type=int, help='number of rounds, which will generate files')
parser.add_argument('--store_folder', '-sf', required=True, help='relative path to folder, where files will be stored')

args = parser.parse_args()
folder_relative_path = args.folder
rounds = args.rounds
store_folder_path = args.store_folder

files_data = []

files = os.listdir(folder_relative_path)
for filename in files:
    with open(f'{folder_relative_path}/{filename}', 'r') as file:
        files_data.append(file.read())

if not os.path.exists(store_folder_path):
    os.makedirs(store_folder_path)
elif not os.path.isdir(store_folder_path):
    print('provided path to store folder isn\'t a directory')
    sys.exit(-1)

total_uploaded_files = len(files_data)

for i in range(rounds):
    file_name = f'{uuid.uuid4()}.txt'

    content = files_data[i % total_uploaded_files]

    with open(f'{store_folder_path}/{file_name}', 'w') as file:
        file.write(content)