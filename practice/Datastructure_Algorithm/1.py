class Solution:
    def twoSum(self,nums,target):
        hash_map = dic()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return i, hash_map[target-x]
            hash_map[x] = i
#链表翻转
def reverseList(self, head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

def reverseList(self, head):

        headNode = ListNode(0)
        while head is not None:
            temp = head.next
            head.next = headNode.next
            headNode.next = head
            head = temp
        return headNode.next

#链表交换相邻元素
def swapPairs(self, head):
    pre, pre.next = self, head:
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a 
    return self.next
#龟兔赛跑判断是否有环
def hasCycle(self, head):
    fast = slow = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

#valid parenthesis
def  isValid(self, s):
    stack = []
    paren_map = {')':'(',']':'[','}':'{'}
    for c in s:
        if c not in paren_map:
            stack.append(c)
        elif not stack or paren_map[c] != stack.pop():
            return False
    return not stack

#valid Anagram
    def isAnagram3(self,s,t):
        return sorted(s) == sorted(t)
  
class Solution:
    def threeSum(self, nums:list[int])->list[list[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >=1 and v == nums[i-1]:
                continue
            d = {}
            for x not in nums[i+1:]:
                if x in d:
                    d[-x-v]=1
                else:
                    res.add((v,-v-x,x))
        return map(list,res)