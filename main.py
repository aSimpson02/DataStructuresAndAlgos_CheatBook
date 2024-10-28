# ##INDEX:

# Section 1 - Arrays, Strings and Linked Lists 
# * Arrays *

#intisialising the array
arr = [1, 2, 3, 4, 5]

#accessing an element
print(arr[2])  # Output: 3

#appending element
arr.append(6)
print(arr)  # Output: [1, 2, 3, 4, 5, 6]

#appending at a certain index
arr.insert(3, 10)
print(arr)  

#output: [1, 2, 3, 10, 4, 5, 6]



# *** SINGLY LINKED LISTS ***


# A Node class below with data part of it in a func 
class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None 


#now we have our node class we can use operations on it, each op = its own func.
#operations on a singly linked list:
# - transversal
# - searching 
# - length
# - insertion [at beginning, end, specific position]
# - deletion [beginning, end, specific node]


#transversal:

    def transversal(head):
        #current (c) node = head 
        c = head

        #transverse = running through each node/ iterating
        while c is not None:
            #print current node
            print(c.data),
        #move to next node
        c = c.next


#searching:

    def searching(head, target):
        #transverse linked list
        while head is not None:
            #if current node's data matches target value
            if head.data == target:
                return True
            #move to next node
            head = head.next


#finding

# = finding total length of a singly LL.

    def finding(head):
        #make length = 0
        l = 0
        c = head
    #transverse/iterate
        while c is not None:
            l += 1
            c += c.next

        return l





#insertion

#part a - insertion at beginning of LL
def insertion_beginning(head, value):
    #create a new node
    new_node = Node(value)

    #set a pointer from new node to current node (= head)
    new_node.next = head

    #move head to point to new node
    head = new_node
    
    return head



#part b - insertion at end of LL
    def insertion_end(head, value):
        new_node = Node(value)
        if head is None:
            return new_node

        c = head
        while c.next is not None:
            c = c.next
        
        c.next = new_node
        
        return head



#part c - at specific point 
    def insertion_specific(head, pos, data):
        new_node = Node(value)

        if  pos == 1:
            new_node = Node(data)
            new_node.next = head
        return new_node
    
        prev = head
        count = 1
        while count < pos-1 and prev is not None:
            prev = prev.next
            count += 1
        
        if prev is None:
            print("invalid pos")
            return head 
        
        new_node - Node(data)
        new_node.next = prev.next
        prev.next = new_node

        return head
    

#deletion of node
#part a - beginning 

    def deletion_beginning(head):
        if not head:
            return None
        temp = head

        head = head.next
        temp = None
        return head



#part b - at end 

    def deletion_end(head):
        if head is None:
            return None

        second_last = head
        while second_last.next.next is not None:
            second_last = second_last.next
        
        second_last.next = None
        return head



#part c - specific pos
    def deletion_specific(head, pos):
        if head is None or pos <1:
            return head
        if pos == 1:
            temp = head
            head = head.next
            temp = None
            return head 
        c = head
        for i in range(1, pos -1):
            if c is not None:
                c = c.next


        



# * Doubly Linked Lists 
# * Circular Linked Lists 


# Section 2 - Stacks and Queues
# * Stacks
# * Queues



# Section 3 - Trees and graphs
# * Binary Tree
# * Binary Search Tree
# * Graphs [Basic and Transversal]



# Section 4 - Sorting and Searching algorithms
# * Sorting: Bubble Sort, Quick Sort, Merge Sort
# * Searching: Linear Search, Binary Search


# Section 5 - Greedy Algorithms
# * Fractional Knapsack Problem



# Section 6 - Dynamic Programming 
# * Fibonacci Sequence