import tomllib

from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
    QVBoxLayout
)
                                                     

class AttributeEditor(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        table = QTableWidget()
        table.setHorizontalHeaderLabels(["Name", "Value"])

        with open("./data/attributes.toml", "rb") as f:
            attributes = tomllib.load(f)

        attribute_list = QTreeWidget()
        attribute_list.setAlternatingRowColors(True)
        attribute_list.setHeaderLabels(["Name", "Type"])

        for name, properties in attributes.items():
            item_name = name
            item_type = properties["type"]
            item = QTreeWidgetItem([item_name, item_type])

            attribute_list.insertTopLevelItem(0, item)

        button = QPushButton("Add new attribute")

        layout = QVBoxLayout()
        layout.addWidget(attribute_list)
        layout.addWidget(button)

        self.setLayout(layout)
