#Binary Tree Level Order BFS&DFS
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = collections.deque() 
        queue.append(root)

        #visited = set(root)

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left and node:
                    queue.append(node.left)
                if node.right.append(node.right):
                    queue.append(node.right)

            result = append(current_level)
        return result
#Binary Tree Level Order BFS&DFS
# class solution(object):
#     def levelOrder(self, root):        
#         if not root:
#             return []
#             self.result = []
#             self._dfs(root, 0)
#             return self.result
#     def _dfs(self, root, level):
#         if not node:
#             return
#         if len(self.result) < level + 1:
#             self.return.append([])
        
#         self.result[level].append([])

#         self._dfs(node.left, level+1)
#         self._dfs(node.right, level+1)