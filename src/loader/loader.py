import requests
import shutil
import multiprocessing
import zipfile
import re

data_dir = 'data'

def _download_file(url):
    local_file = url.split('/')[-1]
    print('Downloading ' + local_file)
    r = requests.get(url, stream=True)
    f = open('data/' + local_file, 'wb')
    shutil.copyfileobj(r.raw, f)
    print('Finished downloading ' + local_file)
    return local_file

def _install_address(one_addr):
    url = 'https://data.openaddresses.io/openaddr-collected-{pkg}'.format(pkg=one_addr)
    local_file = _download_file(url)
    _unzip_file_and_clean(local_file)

def _unzip_file_and_clean(file_name):
    print('Unzipping ' + file_name)
    zf = zipfile.ZipFile('data/' + file_name)
    extractable = filter(lambda f_name: re.match(r'us\/.*\/.*\.csv', f_name), zf.namelist())
    zf.extractall('data', members=extractable)
    print('Finished unzipping ' + file_name)

def install_addresses(address_options):
    p = multiprocessing.Pool(multiprocessing.cpu_count())
    p.map(_install_address, address_options)
    p.close()


if __name__ == '__main__':
    install_addresses(['us_midwest.zip', 'us_northeast.zip'])