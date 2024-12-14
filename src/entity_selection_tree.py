from PySide6.QtWidgets import (
    QTreeWidget,
    QTreeWidgetItem,
    QWidget,
    QVBoxLayout
)
                                                     

class EntitySelectionTree(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        
        placeholder = {
            "Stage 1": [
                "Bush",
                "Slug",
                "Turret"
            ],
            "Stage 2": [
                "Ice",
                "Portal",
                "Turret",
            ]
        }

        tree = QTreeWidget()
        tree.setColumnCount(1)

        items = []
        for stage, entities in placeholder.items():
            item = QTreeWidgetItem([stage])

            for entity in entities:
                child = QTreeWidgetItem([entity])
                item.addChild(child)

            items.append(item)

        tree.insertTopLevelItems(0, items)

        layout = QVBoxLayout()
        layout.addWidget(tree)

        self.setLayout(layout)

