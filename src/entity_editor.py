from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QVBoxLayout
)
                                                     

class EntityEditor(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        entity_image = QPixmap("./finalmaybe.png")
        entity_image_label = QLabel("Blah")
        entity_image_label.setPixmap(entity_image)
        attributes_label   = QLabel("Attributes")
        components_label   = QLabel("Components")
        states_label       = QLabel("States")


        layout = QVBoxLayout()
        layout.addWidget(entity_image_label, 1)
        layout.addWidget(attributes_label, 1)
        layout.addWidget(components_label, 1)
        layout.addWidget(states_label, 1)

        self.setLayout(layout)
