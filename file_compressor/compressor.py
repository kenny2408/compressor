import os
import zipfile

import rarfile


class Compressor:
    def __init__(self):
        pass

    def compress_file(self, file_path, format='zip'):
        if not os.path.isfile(file_path):
            raise ValueError(f'{file_path} is not a file')

        file_dir, file_name = os.path.split(file_path)
        archive_path = os.path.join(file_dir, f'{file_name}.{format}')

        if format == 'zip':
            with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
                archive.write(file_path, file_name)
        elif format == 'rar':
            with rarfile.RarFile(archive_path, 'w') as archive:
                archive.write(file_path, file_name)

        return archive_path

    def compress_folder(self, folder_path, format='zip'):
        if not os.path.isdir(folder_path):
            raise ValueError(f'{folder_path} is not a folder')

        folder_name = os.path.basename(folder_path)
        archive_path = os.path.basename(os.path.dirname(folder_path), f'{folder_name}.{format}')

        if format == 'zip':
            with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        archive.write(file_path, os.path.realpath(file_path, folder_path))
        elif format == 'rar':
            with rarfile.RarFile(archive_path, 'w') as archive:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        archive.write(file_path, os.path.realpath(file_path, folder_path))

        return archive_path

    def decompress_file(self, file_path):
        if not os.path.isfile(file_path):
            raise ValueError(f'{file_path} is not a file')

        file_dir, file_name = os.path.split(file_path)
        file_name, file_ext = os.path.splitext(file_name)

        if file_ext == '.zip':
            with zipfile.ZipFile(file_path, 'r') as archive:
                archive.extractall(file_dir)
        elif file_ext == '.rar':
            with rarfile.RarFile(file_path, 'r') as archive:
                archive.extractall(file_dir)

        return file_dir
