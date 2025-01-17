from Generated.TreeViewer import Ui_MainWindow
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit,
    QLabel, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsTextItem,
    QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QTimer

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeVisualization(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load the design
        self.tree = None
        self.node_count = 0
        self.child_type = None
        self.traversal_steps = []
        self.current_step = 0
        self.addEvents()  # Call the method to connect events
        self.scene = QGraphicsScene()
        self.TreeView.setScene(self.scene)

    def addEvents(self):
        # Connect child buttons to their respective methods
        self.LeftButton.clicked.connect(self.set_left_child)
        self.RightButton.clicked.connect(self.set_right_child)
        self.PreButton.clicked.connect(self.preorder_traversal)
        self.InButton.clicked.connect(self.inorder_traversal)
        self.PostButton.clicked.connect(self.postorder_traversal)

    def set_left_child(self):
        self.child_type = 'L'
        self.add_node()

    def set_right_child(self):
        self.child_type = 'R'
        self.add_node()

    def add_node(self):
        parent_value = self.ParentField.text().strip()
        child_value = self.ChildField.text().strip()

        if not child_value:
            # Adding the root node
            if self.tree is None:
                self.tree = TreeNode(parent_value)
                self.node_count += 1
                self.draw_tree()
                self.show_message("Insert Parent Node and Child Nodes:")
                return
            else:
                self.show_message("Root already exists!")
            return

        if not parent_value or not child_value or not self.child_type:
            self.show_message("Please fill all fields correctly.")
            return

        # Find the parent node
        parent_node = self.find_node(self.tree, parent_value)
        if not parent_node:
            self.show_message(f"Parent node '{parent_value}' not found.")
            return

        # Add the child node
        if self.child_type == "L":
            if parent_node.left is None:
                parent_node.left = TreeNode(child_value)
                self.node_count += 1
            else:
                self.show_message(f"Parent '{parent_value}' already has a left child.")
                return
        elif self.child_type == "R":
            if parent_node.right is None:
                parent_node.right = TreeNode(child_value)
                self.node_count += 1
            else:
                self.show_message(f"Parent '{parent_value}' already has a right child.")
                return

        # Re-draw the tree
        self.draw_tree()
        # self.show_message("Node added successfully.")
        self.ParentField.clear()
        self.ChildField.clear()
        self.child_type = None

    def show_message(self, message):
        """Show a message in a message box."""
        QMessageBox.information(self, "Tree Visualizer", message)

    def find_node(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        left_search = self.find_node(node.left, value)
        if left_search:
            return left_search
        return self.find_node(node.right, value)

    def draw_tree(self):
        self.scene.clear()
        if self.tree:
            self._draw_tree_recursive(self.tree, 400, 50, 200)

    def _draw_tree_recursive(self, node, x, y, offset):
        if node:
            # Draw the node
            ellipse = QGraphicsEllipseItem(x - 15, y - 15, 30, 30)
            ellipse.setBrush(QBrush(Qt.yellow))
            self.scene.addItem(ellipse)

            text = QGraphicsTextItem(node.value)
            text.setPos(x - 10, y - 10)
            self.scene.addItem(text)

            # Draw left and right child nodes
            if node.left:
                self.scene.addLine(x, y, x - offset, y + 100, QPen(Qt.white))
                self._draw_tree_recursive(node.left, x - offset, y + 100, offset // 2)
            if node.right:
                self.scene.addLine(x, y, x + offset, y + 100, QPen(Qt.white))
                self._draw_tree_recursive(node.right, x + offset, y + 100, offset // 2)

    def preorder_traversal(self):
        result = []
        self.traversal_steps = []
        self._preorder(self.tree, result)
        self.current_step = 0
        self.animate_traversal()

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self.traversal_steps.append(node)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def inorder_traversal(self):
        result = []
        self.traversal_steps = []
        self._inorder(self.tree, result)
        self.current_step = 0
        self.animate_traversal()

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self.traversal_steps.append(node)
            self._inorder(node.right, result)

    def postorder_traversal(self):
        result = []
        self.traversal_steps = []
        self._postorder(self.tree, result)
        self.current_step = 0
        self.animate_traversal()

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)
            self.traversal_steps.append(node)

    def animate_traversal(self):
        if self.current_step < len(self.traversal_steps):
            node = self.traversal_steps[self.current_step]
            self.highlight_node(node)
            self.current_step += 1
            self.ResultLabel.setText(f"Traversal Result: {', '.join([n.value for n in self.traversal_steps[:self.current_step]])}")
            QTimer.singleShot(1500, self.animate_traversal)  # Slower speed for better visualization

    def highlight_node(self, node):
        # Highlight the current node in green
        for item in self.scene.items():
            if isinstance(item, QGraphicsEllipseItem):
                item.setBrush(QBrush(Qt.yellow))  # Reset other nodes
            if isinstance(item, QGraphicsTextItem):
                item.setDefaultTextColor(Qt.black)  # Reset text color

        for item in self.scene.items():
            if isinstance(item, QGraphicsTextItem) and item.toPlainText() == node.value:
                for ellipse in self.scene.items():
                    if isinstance(ellipse, QGraphicsEllipseItem) and ellipse.contains(item.sceneBoundingRect().center()):
                        ellipse.setBrush(QBrush(QColor(0, 255, 0)))  # Highlight ellipse
                        break
                item.setDefaultTextColor(QColor(0, 255, 0))  # Highlight text
                break
