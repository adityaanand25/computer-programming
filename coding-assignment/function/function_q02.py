# Rename multiple files in a directory by adding a prefix.

import os
directory = '/path/to/files'
prefix = 'new_'
for filename in os.listdir(directory):
    if not filename.startswith('.'):
        filepath = os.path.join(directory, filename)
        new_filename = prefix + filename
        new_filepath = os.path.join(directory, new_filename)
        os.rename(filepath, new_filepath)
