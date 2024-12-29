class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        # 如果樹是空的，建立根節點
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_helper(self.root, value)
    
    def _insert_helper(self, node, value):
        """
        遞迴方式進行插入：
        - 如果 value 小於 node.value，則插入到左子樹
        - 如果 value 大於 node.value，則插入到右子樹
        """
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_helper(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_helper(node.right, value)
    
    def inorder_traversal(self):
        return self._inorder_traversal_helper(self.root)
    
    def _inorder_traversal_helper(self, node):
        """
        中序遍歷，返回一個包含樹中元素的升冪列表
        """
        if node is None:
            return []
        return self._inorder_traversal_helper(node.left) + [node.value] + self._inorder_traversal_helper(node.right)

# 使用陣列來建立二元搜尋樹
def build_bst_from_array(array):
    bst = BinarySearchTree()
    for value in array:
        bst.insert(value)
    return bst

# 測試代碼
array = [20, 8, 22, 4, 12, 10, 14]
bst = build_bst_from_array(array)

# 輸出中序遍歷結果，應該是升冪順序
print("In-order Traversal:", bst.inorder_traversal())
