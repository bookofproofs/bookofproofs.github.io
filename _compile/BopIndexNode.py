from anytree import AnyNode, RenderTree, ContStyle, PreOrderIter


class BopIndexNode(AnyNode):
    def __init__(self):
        self.label = ""
        self.bop_source = None
        self.count = 0
        super().__init__()

    @staticmethod
    def print(root: AnyNode):
        print(RenderTree(root, style=ContStyle()))

    @staticmethod
    def get_bop_sources_in_pre_order(root: AnyNode):
        return list(filter(lambda b: b is not None, list(node.bop_source for node in PreOrderIter(root))))

    @staticmethod
    def clear(root):
        for child in root.children:
            BopIndexNode._remove_node_recursively(child)

    @staticmethod
    def _remove_node_recursively(node):
        for child in node.children:
            BopIndexNode._remove_node_recursively(child)
        if len(node.children) == 0:
            node.parent = None
            del node

