class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def append_at_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            new_node=self.head
            return
            
        curr = self.head
        while curr.next:
            curr=curr.next

        curr.next=new_node

        
    def print_linked_list(self):
        if self.head is None:
            print("empty list")
        
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        
        print("None")

ll=linked_list()
ll.append_at_end(1)
ll.append_at_end(2)
ll.append_at_end(3)
ll.print_linked_list()
