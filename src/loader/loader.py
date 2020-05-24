import requests
import shutil
import multiprocessing
import zipfile
import re
import os
from pathlib import Path
import glob
from mun import Mun

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
    os.remove('data/' + file_name)

def install_addresses(address_options):
    cores = multiprocessing.cpu_count()
    print('Running with {c} processes'.format(c=cores))
    p = multiprocessing.Pool(cores)
    # p.map(_install_address, address_options)
    p.map(_run_insert, glob.glob('data/us/**/*.csv'))
    p.close()

def _run_insert(file_path:str) -> None:
    m = Mun(file_path)
    m.insert_self()

if __name__ == '__main__':
    install_addresses(['us_midwest.zip', 'us_northeast.zip'])
    # print(glob.glob('data/us/**/*.csv'))
