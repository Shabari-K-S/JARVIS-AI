from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import QPixmap, QColor, QPainter, QBrush, QFont, QPen
from PyQt5.QtCore import Qt

class LayeredImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(400, 400)
        self.state = 'idle'
        self.arc_color = QColor(255, 255, 255)
        self.load_images()
        self.center_on_screen()

    def load_images(self):
        image_files = ["jarvis/assets/circle-bottom.png", "jarvis/assets/circle-middle.png", "jarvis/assets/circle-top.png"]
        self.labels = []
        for image_file in image_files:
            label = QLabel(self)
            pixmap = QPixmap(image_file)
            label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            label.setGeometry(0, 0, 400, 400)
            self.labels.append(label)
        self.update()

    def center_on_screen(self):
        screen = QApplication.primaryScreen().availableGeometry().center()
        self.move(screen.x() - self.width() // 2, screen.y() - self.height() // 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw background circle
        brush = QBrush(QColor(0, 0, 0, 128))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, 400, 400)

        # Set arc color based on state
        self.set_arc_color()

        # Draw arcs
        self.draw_arcs(painter)

        # Draw text
        self.draw_text(painter)

    def set_arc_color(self):
        color_map = {
            'idle': QColor(255, 255, 255),
            'listening': QColor(255, 255, 255),
            'recognizing': QColor(255, 255, 0),
            'recognized': QColor(0, 255, 0),
            'not_recognized': QColor(255, 0, 0)
        }
        self.arc_color = color_map.get(self.state, QColor(255, 255, 255))

    def draw_arcs(self, painter):
        pen = QPen(self.arc_color, 5)
        painter.setPen(pen)
        small_rect = 55, 55, 290, 290
        for i in range(4):
            painter.drawArc(small_rect[0], small_rect[1], small_rect[2], small_rect[3], (i * 90 * 16) - 980, 90 * 8 - 200)

    def draw_text(self, painter):
        painter.setPen(QColor(250, 250, 230))
        font = QFont("Arial", 30, QFont.Bold)
        painter.setFont(font)
        text = "J.A.R.V.I.S."
        text_rect = painter.boundingRect(self.rect(), Qt.AlignCenter, text)
        painter.drawText(text_rect, Qt.AlignCenter, text)

    def closeEvent(self, event):
        print("Window is closing, shutting down the application.")
        super().closeEvent(event)

