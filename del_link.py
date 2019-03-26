# coding=utf-8
import logging
import os
import shutil
import tempfile
import time
import re


def del_link(file):
    p = re.compile('https://raw\.githubusercontent\.com/jdegre/5GC_APIs/\w+/')
    lines = []
    with open(file, 'rt', encoding='utf-8') as fin:
        for line in fin.readlines():
            lines.append(p.sub('', line, 1))
    with open(file, 'wt', encoding='utf-8') as fout:
        for line in lines:
            fout.write(line)


def main():
    start_time = time.time()
    for root, _, files in os.walk('.'):
        if root == '.':
            for file in files:
                if file.endswith('.yaml'):
                    del_link(file)
    print('{:.3}s'.format(time.time() - start_time))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.exception(e)