#!/usr/bin/env python

import os
import time
import gzip
import shutil

directory = '/home/jack/files'

compress = 10
delete = 20
compress_path = compress * 24 * 60 * 60
delete_path = delete * 24 * 60 * 60
now = time.time()

for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        files_age = now - os.path.getmtime(path)
        
        if files_age > delete_path:
            try:
                os.remove(path)
                print(f"Deleted: {path}")
            except Exception as e:
                print(f"Error deleting files {path}: {e}")
        
        elif files_age > compress_path and not filename.endswith('.gz'):
            gz_path = path + '.gz'
            try:
                with open(path, 'rb') as f_in:
                    with gzip.open(gz_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(path)
                print(f"Compressed: {path}")
            except Exception as e:
                print(f"Error compressing files {path}: {e}")
