import argparse
import requests
import os

# 'http://localhost:5001/file/upload' or 'http://localhost:5002/structured-data/upload'

def send_file(file_name, url, file_field_name, data):
    # TODO: find out if sql dump can be send as 'rb'
    f = open(file_name, 'rb')
    files = { file_field_name: f }

    response = requests.post(url, files=files, data=data)

    print(f'Response status code: {response.status_code} for file: {file_name}')
    message = response.json()['message']
    print(f'Response message: {message}')

    f.close()


parser = argparse.ArgumentParser()
parser.add_argument('--url', '-u', required=True, help='url on which will be the data send')
parser.add_argument('--file', '-f', default=None, help='path to the file, which will be uploaded on the url')
parser.add_argument('--directory', '-d', default=None,
    help='path to the directory with files, which will be uploaded on the url')
parser.add_argument('--type', '-t', required=True, choices=['structured', 'unstructured'],
    help='type of the data, which will be uploade (structured or unstructured)')
parser.add_argument('--min_size', '-m', type=int, default=64,
    help='possible min size of the chunk, which will be created from unstructured data')
parser.add_argument('--avg_size', '-a', type=int, default=256,
    help='avg size of the chunk, which will be created from unstructured data')
parser.add_argument('--max_size', '-s', type=int, default=1024,
    help='possible max size of the chunk, which will be created from unstructured data')


args = parser.parse_args()
url = args.url
data_type = args.type

data = { 'min_size': args.min_size, 'avg_size': args.avg_size, 'max_size': args.max_size } \
    if data_type == 'unstructured' else {}
file_field_name = 'file' if data_type == 'unstructured' else 'sql_dump'


if args.file:
    file_relative_path = args.file

    if os.path.exists(file_relative_path):
        send_file(file_relative_path, url, file_field_name, data)
    else:
        print(f'File: {file_relative_path} doesn\'t exists.')

elif args.directory:
    directory = args.directory

    if not os.path.exists(directory):
        print(f'Directory: {directory} doesn\'t exists.')
    else:
        files_names = os.listdir(directory)
        for file_name in files_names[:10]:
            file_relative_path = f'{directory}/{file_name}'
            send_file(file_relative_path, url, file_field_name, data)

else:
    print('Provide either relative path to file or directory, which contains files for upload. \n' +
        + 'Use -f <relative_path_to_file> or -d <relative_path_to_directory_with_files>')