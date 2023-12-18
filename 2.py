class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def llToNum(ll):
    vals = []
    c = ll
    while c is not None:
        vals.append(c.val)
        c = c.next

    return sum([10**i * vals[i] for i in range(len(vals))])

def numToLL(num):
    """stringwise because I can't think of anything more elegant right now"""
    digits = list(str(num))[::-1] # array of strs
  

    head = ListNode(digits[0])
    current_node = head

    for digit in digits[1:]: # skip head value
        current_node.next = ListNode(digit)
        current_node = current_node.next
    
    return head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return numToLL(llToNum(l1) + llToNum(l2))