import requests, shutil, multiprocessing, zipfile, re, os, time
from pathlib import Path
from typing import List
import glob
from functools import partial
from src.loader.mun import Mun
from src.models.address import address

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
    if cores <= 1:
        cores = 2
    print('Running with {c} processes'.format(c=cores))
    p = multiprocessing.Pool(cores)
    # p.map(_install_address, address_options)
    q = multiprocessing.Manager().Queue()
    p.map_async(_run_insert, [(q, fp) for fp in glob.glob('data/us/**/*.csv')])
    has_items = True
    id = 0
    while has_items:
        try:
            addr: address = q.get(block=True, timeout=60)
            addr.rowid = id
            addr.insert()
            id += 1
        except Exception:
            has_items = False
    p.close()

def _run_insert(args) -> None:
    q = args[0]
    file_path = args[1]
    m = Mun(file_path)
    addrs: List[address] = m.parse_addresses()
    for a in addrs:
        if a.is_valid:
            q.put(a)

# if __name__ == '__main__':
    # print(glob.glob('data/us/**/*.csv'))
