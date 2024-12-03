Write a program to compress a text file using gzip.

import gzip
def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            f_out.writelines(f_in)
compress_file('example.txt', 'example.txt.gz')
