#!/usr/bin/env python3
"""
Modern Image Converter
Convert images to WebP, AVIF, JPEG, PNG
Cross-platform: Windows, macOS, Linux
"""

import sys
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFileDialog,
                             QComboBox, QSlider, QProgressBar, QListWidget,
                             QGroupBox, QSpinBox, QMessageBox)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QIcon, QFont, QPalette, QColor, QDragEnterEvent, QDropEvent
from PIL import Image
import os

class ConversionWorker(QThread):
    """Worker thread để convert ảnh không block UI"""
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, files, output_format, quality, output_dir):
        super().__init__()
        self.files = files
        self.output_format = output_format
        self.quality = quality
        self.output_dir = output_dir

    def run(self):
        total = len(self.files)
        success_count = 0

        for idx, file_path in enumerate(self.files):
            try:
                img = Image.open(file_path)

                # Convert RGBA to RGB nếu cần cho JPEG
                if self.output_format.upper() == 'JPEG' and img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background

                # Tạo output filename
                input_name = Path(file_path).stem
                output_ext = self.output_format.lower()
                if output_ext == 'jpeg':
                    output_ext = 'jpg'
                output_path = os.path.join(self.output_dir, f"{input_name}.{output_ext}")

                # Save với settings phù hợp
                save_kwargs = {'quality': self.quality}

                if self.output_format.upper() == 'WEBP':
                    save_kwargs['method'] = 6  # Best compression
                elif self.output_format.upper() == 'AVIF':
                    save_kwargs['speed'] = 4  # Balance speed/quality
                elif self.output_format.upper() == 'PNG':
                    save_kwargs = {'optimize': True}

                img.save(output_path, self.output_format.upper(), **save_kwargs)
                success_count += 1

            except Exception as e:
                self.error.emit(f"Error converting {Path(file_path).name}: {str(e)}")

            self.progress.emit(int((idx + 1) / total * 100))

        self.finished.emit(f"Successfully converted {success_count}/{total} images to {self.output_format}")


class ImageConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_files = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Modern Image Converter")
        self.setGeometry(100, 100, 900, 700)
        self.setAcceptDrops(True)

        # Dark modern theme
        self.set_dark_theme()

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Title
        title = QLabel("🖼️ Modern Image Converter")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # File selection area
        file_group = QGroupBox("📁 Select Images")
        file_group.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        file_layout = QVBoxLayout()

        btn_layout = QHBoxLayout()
        self.btn_select_files = QPushButton("Select Files")
        self.btn_select_files.setMinimumHeight(45)
        self.btn_select_files.clicked.connect(self.select_files)

        self.btn_clear = QPushButton("Clear All")
        self.btn_clear.setMinimumHeight(45)
        self.btn_clear.clicked.connect(self.clear_files)

        btn_layout.addWidget(self.btn_select_files)
        btn_layout.addWidget(self.btn_clear)
        file_layout.addLayout(btn_layout)

        # File list
        self.file_list = QListWidget()
        self.file_list.setMinimumHeight(200)
        file_layout.addWidget(self.file_list)

        drag_label = QLabel("💡 Tip: Drag & drop images here")
        drag_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        drag_label.setStyleSheet("color: #888; font-style: italic;")
        file_layout.addWidget(drag_label)

        file_group.setLayout(file_layout)
        main_layout.addWidget(file_group)

        # Settings area
        settings_group = QGroupBox("⚙️ Conversion Settings")
        settings_group.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        settings_layout = QVBoxLayout()

        # Format selection
        format_layout = QHBoxLayout()
        format_label = QLabel("Output Format:")
        format_label.setFont(QFont("Arial", 11))
        self.format_combo = QComboBox()
        self.format_combo.addItems(["WebP", "AVIF", "JPEG", "PNG"])
        self.format_combo.setMinimumHeight(35)
        self.format_combo.setFont(QFont("Arial", 11))
        format_layout.addWidget(format_label)
        format_layout.addWidget(self.format_combo)
        format_layout.addStretch()
        settings_layout.addLayout(format_layout)

        # Quality slider
        quality_layout = QVBoxLayout()
        quality_label_layout = QHBoxLayout()
        quality_label = QLabel("Quality:")
        quality_label.setFont(QFont("Arial", 11))
        self.quality_value = QLabel("85")
        self.quality_value.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        quality_label_layout.addWidget(quality_label)
        quality_label_layout.addWidget(self.quality_value)
        quality_label_layout.addStretch()
        quality_layout.addLayout(quality_label_layout)

        self.quality_slider = QSlider(Qt.Orientation.Horizontal)
        self.quality_slider.setMinimum(1)
        self.quality_slider.setMaximum(100)
        self.quality_slider.setValue(85)
        self.quality_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.quality_slider.setTickInterval(10)
        self.quality_slider.valueChanged.connect(self.update_quality_label)
        quality_layout.addWidget(self.quality_slider)

        settings_layout.addLayout(quality_layout)
        settings_group.setLayout(settings_layout)
        main_layout.addWidget(settings_group)

        # Output directory
        output_group = QGroupBox("📂 Output Directory")
        output_group.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        output_layout = QHBoxLayout()

        self.output_label = QLabel("Same as source")
        self.output_label.setStyleSheet("color: #4CAF50;")
        self.btn_output_dir = QPushButton("Change Output Dir")
        self.btn_output_dir.setMinimumHeight(40)
        self.btn_output_dir.clicked.connect(self.select_output_dir)

        output_layout.addWidget(self.output_label, 1)
        output_layout.addWidget(self.btn_output_dir)
        output_group.setLayout(output_layout)
        main_layout.addWidget(output_group)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimumHeight(30)
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

        # Convert button
        self.btn_convert = QPushButton("🚀 Convert Images")
        self.btn_convert.setMinimumHeight(60)
        self.btn_convert.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.btn_convert.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QPushButton:disabled {
                background-color: #666;
            }
        """)
        self.btn_convert.clicked.connect(self.convert_images)
        main_layout.addWidget(self.btn_convert)

        # Status label
        self.status_label = QLabel("Ready to convert")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont("Arial", 10))
        self.status_label.setStyleSheet("color: #888;")
        main_layout.addWidget(self.status_label)

        self.output_dir = None

    def set_dark_theme(self):
        """Set modern dark theme"""
        dark_stylesheet = """
            QMainWindow {
                background-color: #1e1e1e;
            }
            QWidget {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QGroupBox {
                border: 2px solid #444;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 15px;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 5px;
            }
            QPushButton {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #555;
                border-radius: 6px;
                padding: 8px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #3d3d3d;
                border: 1px solid #777;
            }
            QPushButton:pressed {
                background-color: #1d1d1d;
            }
            QComboBox {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #555;
                border-radius: 6px;
                padding: 5px;
            }
            QComboBox:hover {
                border: 1px solid #777;
            }
            QComboBox::drop-down {
                border: none;
            }
            QListWidget {
                background-color: #2d2d2d;
                border: 1px solid #555;
                border-radius: 6px;
            }
            QSlider::groove:horizontal {
                height: 8px;
                background: #2d2d2d;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #4CAF50;
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
            QProgressBar {
                border: 1px solid #555;
                border-radius: 6px;
                text-align: center;
                background-color: #2d2d2d;
            }
            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 5px;
            }
        """
        self.setStyleSheet(dark_stylesheet)

    def update_quality_label(self, value):
        self.quality_value.setText(str(value))

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Images",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp *.avif);;All Files (*.*)"
        )
        if files:
            self.selected_files.extend(files)
            self.update_file_list()

    def clear_files(self):
        self.selected_files.clear()
        self.file_list.clear()
        self.status_label.setText("Ready to convert")

    def update_file_list(self):
        self.file_list.clear()
        for file in self.selected_files:
            self.file_list.addItem(Path(file).name)
        self.status_label.setText(f"{len(self.selected_files)} file(s) selected")

    def select_output_dir(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if directory:
            self.output_dir = directory
            self.output_label.setText(f"...{directory[-40:]}")

    def convert_images(self):
        if not self.selected_files:
            QMessageBox.warning(self, "No Files", "Please select images to convert!")
            return

        output_format = self.format_combo.currentText()
        quality = self.quality_slider.value()

        # Determine output directory
        if self.output_dir:
            output_dir = self.output_dir
        else:
            output_dir = str(Path(self.selected_files[0]).parent)

        # Disable buttons during conversion
        self.btn_convert.setEnabled(False)
        self.btn_select_files.setEnabled(False)
        self.status_label.setText(f"Converting to {output_format}...")

        # Start conversion in background thread
        self.worker = ConversionWorker(self.selected_files, output_format, quality, output_dir)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished.connect(self.conversion_finished)
        self.worker.error.connect(self.conversion_error)
        self.worker.start()

    def conversion_finished(self, message):
        self.status_label.setText(message)
        self.btn_convert.setEnabled(True)
        self.btn_select_files.setEnabled(True)
        self.progress_bar.setValue(100)
        QMessageBox.information(self, "Success", message)

    def conversion_error(self, error_msg):
        self.status_label.setText(f"Error: {error_msg}")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        image_files = [f for f in files if f.lower().endswith(
            ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp', '.avif')
        )]
        if image_files:
            self.selected_files.extend(image_files)
            self.update_file_list()


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Modern look across platforms
    window = ImageConverterApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
