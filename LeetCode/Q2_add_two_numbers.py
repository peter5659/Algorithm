class ListNode():
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
        self.first = self
        self.final = self
    def append(self, data):
        new_node = ListNode(data)
        self.final.next = new_node
        self.final = self.final.next

class Solution():
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2: return None
        ret = ListNode()
        ret.val = ((l1.val if l1 else 0) + (l2.val if l2 else 0)) % 10
        
        if ((l1.val if l1 else 0) + (l2.val if l2 else 0)) // 10 == 1:
            if l1.next:
                l1.next.val += 1
            else:
                l1.next = ListNode(val=1)
            
        ret.next = self.addTwoNumbers((l1.next if l1 else None), (l2.next if l2 else None))
        
        return ret
        
list1 = ListNode()
list1.val = 2
list1.append(5)
list1.append(3)

list2 = ListNode()
list2.val = 4
list2.append(5)
list2.append(3)


a = Solution()
alist = a.addTwoNumbers(list1,list2)
what = alist
while(what):
    print(what.val)
    what = what.next












