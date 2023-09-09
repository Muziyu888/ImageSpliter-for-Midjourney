from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QGraphicsScene, QMessageBox
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor
from PySide6.QtCore import QTimer, Qt
import os
import sys
from PIL import Image
import time
import multiprocessing
from multiprocessing import Pool
from Ui_untitled import Ui_Form

def split_image(image_path, rows, cols, image_format, output_directory):
    img = Image.open(image_path)
    w, h = img.size
    row_height = h // rows
    col_width = w // cols
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    
    if image_format == '原格式':
        image_format = img.format

    for i in range(rows):
        for j in range(cols):
            left = j * col_width
            upper = i * row_height
            right = left + col_width
            lower = upper + row_height
            img_cropped = img.crop((left, upper, right, lower))
            output_path = os.path.join(output_directory, f"{base_name}_{i}_{j}.{image_format.lower()}")
            img_cropped.save(output_path, image_format.upper() if image_format != 'JPG' else 'JPEG')

class ImageSplitterApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.resize_timer = QTimer(self)
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self.handle_resize_timeout)
   
        self.pushButton.clicked.connect(self.load_images)
        self.pushButton_2.clicked.connect(self.load_folder)
        self.pushButton_3.clicked.connect(self.select_output_folder)
        self.pushButton_4.clicked.connect(self.start_splitting)
        
        self.pushButton_5.clicked.connect(self.previous_image)
        self.pushButton_6.clicked.connect(self.next_image)

        self.spinBox.valueChanged.connect(self.update_graphics_view)
        self.spinBox_2.valueChanged.connect(self.update_graphics_view)

        self.selected_images = []
        self.output_directory = None
        self.current_image_index = 0

        self.graphics_scene = QGraphicsScene(self)
        self.graphicsView.setScene(self.graphics_scene)
        
        self.setAcceptDrops(True)

    def load_images(self):
        self.current_image_index = 0
        options = QFileDialog.Options()
        file_names, _ = QFileDialog.getOpenFileNames(self, "Select Image(s)", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.ico);;All Files (*)", options=options)
        
        if file_names:
            self.selected_images = file_names
            
            self.lineEdit.setText(';'.join(file_names))
            self.display_image(self.selected_images[0])
            self.update_graphics_view()       
            self.update_image_label()
    
    def load_folder(self):
        self.current_image_index = 0
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        
        if folder_path:
            image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.ico'))]
            self.selected_images = [os.path.join(folder_path, img_file) for img_file in image_files]
            self.lineEdit.setText(folder_path)
            
            if self.selected_images:
                self.display_image(self.selected_images[0])
                self.update_graphics_view()
                self.update_image_label()
        
    def update_image_label(self):
        self.label_5.setText(f"{self.current_image_index + 1} / {len(self.selected_images)}")
    
    def select_output_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_path:
            self.output_directory = folder_path
            self.lineEdit_2.setText(folder_path)
            
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_timer.start(50)
             
    def handle_resize_timeout(self):
        if self.selected_images:
            self.display_image(self.selected_images[self.current_image_index])
            
    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(self.graphicsView.width() - 5, self.graphicsView.height() - 5, Qt.KeepAspectRatio)
        
        self.graphics_scene.clear()
        self.graphics_scene.addPixmap(pixmap)
        self.graphicsView.setScene(self.graphics_scene)
        self.graphicsView.setSceneRect(pixmap.rect())
        self.update_graphics_view()
    
    def update_graphics_view(self):
        if not self.selected_images:
            return

        image_path = self.selected_images[self.current_image_index]
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(self.graphicsView.width() - 5, self.graphicsView.height() - 5, Qt.AspectRatioMode.KeepAspectRatio)
        painter = QPainter(pixmap)

        pen = QPen()
        pen.setColor(QColor(0, 255, 0))  # 设置为荧光绿色，使用 RGB 值
        # 或者使用 HTML 颜色代码：pen.setColor(QColor("#00FF00"))
        pen.setWidth(2)  # 设置线宽为3像素
        pen.setStyle(Qt.PenStyle.DashDotLine)  # 设置线型为 Dash-Dot Line

        painter.setPen(pen)

        rows = self.spinBox.value()
        cols = self.spinBox_2.value()
        w, h = pixmap.width(), pixmap.height()

        row_height = h // rows
        col_width = w // cols

        for i in range(1, rows):
            painter.drawLine(0, i * row_height, w, i * row_height)
        for i in range(1, cols):
            painter.drawLine(i * col_width, 0, i * col_width, h)

        painter.end()

        self.graphics_scene.clear()
        self.graphics_scene.addPixmap(pixmap)
        self.graphicsView.setScene(self.graphics_scene)

    def start_splitting(self):
        if not self.selected_images or not self.output_directory:
            return

        rows = self.spinBox.value()
        cols = self.spinBox_2.value()

        format_group = [self.radioButton, self.radioButton_2, self.radioButton_3]
        image_format = 'JPEG'
        for btn in format_group:
            if btn.isChecked():
                image_format = btn.text()

        start_time = time.time()

        with Pool() as pool:
            pool.starmap(split_image, [(img_path, rows, cols, image_format, self.output_directory) for img_path in self.selected_images])

        end_time = time.time()

        elapsed_time = round(end_time - start_time, 2)
        QMessageBox.information(self, "成功", f"切割成功图片成功 \n共切割 {len(self.selected_images)} 张图片 \n花费 {elapsed_time} 秒.")
                   
    def previous_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.selected_images)
        self.display_image(self.selected_images[self.current_image_index])
        self.update_image_label()

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.selected_images)
        self.display_image(self.selected_images[self.current_image_index])
        self.update_image_label()              
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.selected_images = []
        urls = event.mimeData().urls()
        image_files = []
        folder_files = []
        for url in urls:
            path = url.toLocalFile()
            file_extension = os.path.splitext(path)[-1].lower()
            if os.path.isfile(path) and file_extension in [
                '.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.ico'
                ]:
                image_files.append(path)
            elif os.path.isdir(path):
                folder_files.append(path)
        
        if image_files:
            self.load_dragged_images(image_files)
        if folder_files:
            for folder in folder_files:
                self.load_dragged_folder(folder)

    def load_dragged_images(self, image_files):
        self.current_image_index = 0
        self.selected_images.extend(image_files)
        self.lineEdit.setText(';'.join(self.selected_images))
        self.display_image(self.selected_images[0])
        self.update_graphics_view()
        self.update_image_label()

    def load_dragged_folder(self, folder_path):
        self.current_image_index = 0
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.ico'))]
        self.selected_images.extend([os.path.join(folder_path, img_file) for img_file in image_files])
        self.lineEdit.setText(folder_path)
        if self.selected_images:
            self.display_image(self.selected_images[0])
            self.update_graphics_view()
        self.update_image_label()
        
if __name__ == "__main__":   
    
    multiprocessing.freeze_support()
    multiprocessing.set_start_method('spawn')
    
    app = QApplication(sys.argv)
    mainWin = ImageSplitterApp()
    mainWin.show()
    sys.exit(app.exec())