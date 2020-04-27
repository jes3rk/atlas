import requests
import shutil
import multiprocessing
import os

def _download_file(url):
    r = requests.get(url, stream=True)
    local_file = url.split('/')[-1]
    f = open('data/' + local_file, 'wb')
    shutil.copyfileobj(r.raw, f)
    return local_file

def _install_address(one_addr):
    url = 'https://data.openaddresses.io/openaddr-collected-{pkg}'.format(pkg=one_addr)
    #local_file = _download_file(url)
    _unzip_file('data/us_midwest.zip')

def _unzip_file(file_name):
    pass


def install_addresses(address_options):
    p = multiprocessing.Pool(multiprocessing.cpu_count)
    p.map(_install_address, address_options)
    p.join()
    p.close()


if __name__ == '__main__':
    install_addresses(['us_midwest.zip'])