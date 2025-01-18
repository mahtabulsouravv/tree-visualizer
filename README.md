# Tree Visualizer

A Python-based GUI application to visualize binary trees using PyQt5. The Tree Visualizer allows users to:

- Add nodes to a binary tree dynamically.
- Visualize the tree structure in real-time.
- Perform and animate Pre-order, In-order, and Post-order traversals.

## Features

1. **Add Nodes**: 
   - Specify the parent node and child node value(Number or String).
   - Indicate whether the child is on the left (L) or right (R) side.
   - Add up to 31 nodes.

2. **Tree Visualization**:
   - Automatically redraws the tree whenever a new node is added.

3. **Tree Traversal Animations**:
   - Pre-order, In-order, and Post-order traversals are animated.
   - Nodes are highlighted sequentially during traversal.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mahtabulsouravv/tree-visualizer.git
   cd tree-visualizer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using:
```bash
python RunTree.py
```

### Adding Nodes
- Enter the **Parent Node** value.
- Enter the **Child Node** value.
- Specify the **Child Type** as `Left` or `Right` by Buttons .

### Traversals
- Use the **PreOrder Traversal**, **InOrder Traversal**, or **PostOrder Traversal** buttons to visualize traversals.

## Preview

![Tree Visualizer](https://github.com/mahtabulsouravv/tree-visualizer/blob/main/Resources/Preview.PNG)


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements.
