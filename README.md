## How to run
* python -m venv ./venv
* ./venv/Scripts/activate
* pip install -r requirements.txt
* python ./automatic_upload.py <required_arguments>

## Command line arguments explained
* --url/-u = url on which will be the data send
* --file/-f = relative path to file, which will be send to the url
* --directory/-d = relativie path to directory with files, which will be send to the url
* --type/-t = type of the data, which will be uploaded (only chocies: structured/unstructured)
* --min_size/-m = possible min size of the chunk, which will be created from unstructured data
* --avg_size/-a = avg size of the chunk, which will be created from unstructured data
* --max_size/-m = possible max size of the chunk, which will be created from unstructured data


## Upload
### Prerequisites
Running [infrastructure](https://github.com/diplomovka/infrastructure) in Docker

### Structured data example
python ./automatic_upload.py -u http://localhost:5002/structured-data/upload -f test.sql -t structured

### Unstructured data
python ./automatic_upload.py -u http://localhost:5001/file/upload -f test.txt -t unstructured
