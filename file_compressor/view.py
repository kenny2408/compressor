from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox


class View(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('File Compressor')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(400, 200)

        # Set dark style sheet
        self.setStyleSheet('''
            QWidget {
                background-color: #212F3F;
                color: #ADBBC9;
                font-family: Arial;
                font-size: 12px;
            }
            QLabel {
                font-weight: bold;
                margin-bottom: 5px;
            }
            QLineEdit {
                background-color: #2D3947;
                color: #ADBBC9;
                border-radius: 3px;
                padding: 3px;
            }
            QPushButton {
                background-color: #39434F;
                color: #ADBBC9;
                border-radius: 3px;
                padding: 5px;
                min-width: 50px;
            }
            QPushButton:hover {
                background-color: #444D57;
            }
        ''')

        # Create central widget
        central_widget = QWidget()

        # Create layout for central widget
        main_layout = QVBoxLayout()

        # Create input fields and button
        self.file_path_input = QLineEdit()
        self.file_path_input.setPlaceholderText('Select a file...')
        self.file_path_button = QPushButton('...')

        self.folder_path_input = QLineEdit()
        self.folder_path_input.setPlaceholderText('Select a folder...')
        self.folder_path_button = QPushButton('...')

        self.compress_file_button = QPushButton('Compress File')
        self.compress_folder_button = QPushButton('Compress Folder')

        self.decompress_file_button = QPushButton('Decompress File')

        # Add input fields and button to layout
        main_layout.addWidget(QLabel('File'))

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_path_input)
        file_layout.addWidget(self.file_path_button)

        main_layout.addLayout(file_layout)
        main_layout.addWidget(QLabel('Folder'))

        folder_layout =QHBoxLayout()
        folder_layout.addWidget(self.folder_path_input)
        folder_layout.addWidget(self.folder_path_button)

        main_layout.addLayout(file_layout)
        main_layout.addWidget(self.compress_file_button)
        main_layout.addWidget(self.compress_folder_button)
        main_layout.addWidget(self.decompress_file_button)

        # Set layout for central widget and set as central widget
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect button signals to slots
        self.file_path_button.clicked.connect(self.select_file_path)
        self.folder_path_button.clicked.connect(self.select_folder_path)

    def select_file_path(self):
        file_path = QFileDialog.getOpenFileName(self, 'Select File')
        if file_path:
            self.file_path_input.setText(file_path)

    def select_folder_path(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder_path:
            self.folder_path_input.setText(folder_path)

    def show_error(self, message):
        QMessageBox.critical(self, 'Error', message)

    def show_success(self, message):
        QMessageBox.information(self, 'Success', message)

    def clear_inputs(self):
        self.file_path_input.clear()
        self.folder_path_input.clear()
