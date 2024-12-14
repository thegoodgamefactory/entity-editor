import sys
from PySide6.QtCore import QRect
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget
from attribute_editor import AttributeEditor
from entity_editor import EntityEditor
from entity_selection_tree import EntitySelectionTree

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        menu = self.menuBar()
        menu.addMenu("&File")
        menu_actions = menu.addMenu("&Menus")

        button_action = QAction(QIcon("bug.png"), "&Attribute Editor", self)
        button_action.setStatusTip("Opens the attribute editor menu")
        button_action.triggered.connect(self.open_attribute_editor)

        menu_actions.addAction(button_action)
        self.attribute_editor = None

        layout = QHBoxLayout()
        layout.addWidget(EntitySelectionTree(), 1)
        layout.addWidget(EntityEditor(), 4)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_attribute_editor(self):
        self.attribute_editor = AttributeEditor()
        self.attribute_editor.setGeometry(QRect(100, 100, 300, 300))
        self.attribute_editor.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
