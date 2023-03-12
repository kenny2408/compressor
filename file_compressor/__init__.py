import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from compressor import Compressor
from view import View


class Controller:
    def __init__(self, view, compressor):
        self.view = view
        self.compressor = compressor
        self.connect_signals()

    def connect_signals(self):
        self.view.compress_file_button.clicked.connect(self.compress_file)
        self.view.compress_folder_button.clicked.connect(self.compress_folder)
        self.view.decompress_file_button.clicked.connect(self.decompress_file)

    def compress_file(self):
        file_path = self.view.file_path_input.text()

        if not file_path:
            self.view.show_error('Please select a file to compress')
            return

        try:
            archive_path = self.compressor.compress_file(file_path)
            self.view.show_success(f'{file_path} compressed to {archive_path}')
            self.view.clear_inputs()
        except Exception as e:
            self.view.show_error(str(e))

    def compress_folder(self):
        folder_path = self.view.folder_path_input.text()

        if not folder_path:
            self.view.show_error('Please select a folder to compress')
            return

        try:
            archive_path = self.compressor.compress_folder(folder_path)
            self.view.show_success(f'{folder_path} compress to {archive_path}')
            self.view.clear_inputs()
        except Exception as e:
            self.view.show_error(str(e))

    def decompress_file(self):
        file_path = self.view.file_path_input.txt()

        if not file_path:
            self.view.show_error('Please select a file to decompress')
            return

        try:
            extracted_path = self.compressor.decompress_file(file_path)
            self.view.show_success(f'{file_path} decompress to {extracted_path}')
            self.view.clear_inputs()
        except Exception as e:
            self.view.show_error(str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('File Compressor')
    app.setWindowIcon(QIcon('icon.png'))

    view = View()
    compressor = Compressor()
    controller = Controller(view, compressor)

    view.show()
    sys.exit(app.exec_())
