# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.string = ""

        def dfs(node):
            if node is None:
                self.string += "N,"
            else:
                self.string += str(node.val) + ","
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        
        return self.string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        self.index = 0

        if data == "N,":
            return None
        
        for i in range(self.index, len(data)):
            if data[i] == ",":
                self.final_index = i
                break
        
        number_to_add = int(data[self.index:self.final_index])
        root = TreeNode(number_to_add)
        self.index = self.final_index+1

        def creator(node):
            if self.index == len(data):
                return

            if data[self.index:self.index+2] != "N,":

                for i in range(self.index, len(data)):
                    if data[i] == ",":
                        self.final_index = i
                        break
                
                number_to_add = int(data[self.index:self.final_index])
                node.left = TreeNode(number_to_add)
                self.index = self.final_index+1
                creator(node.left)

            else:
                self.index += 2
            
            if data[self.index:self.index+2] != "N,":

                for i in range(self.index, len(data)):
                    if data[i] == ",":
                        self.final_index = i
                        break
                
                number_to_add = int(data[self.index:self.final_index])
                node.right = TreeNode(number_to_add)
                self.index = self.final_index+1
                creator(node.right)

            else:
                self.index += 2

        creator(root)

        return root
