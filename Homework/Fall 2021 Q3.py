from DoublyLinkedList import *

def set_grade(grades_lst, netID, grade):
    inside = False
    node = grades_lst.header.next
    for i in range (len(grades_lst)):
        if netID == node.data[0]:
            inside = True
            node.data = (netID, grade)
        node = node.next
    
    if inside == False:
        node_prev = grades_lst.trailer.prev
        node_next = grades_lst.trailer
        new_node = DoublyLinkedList().Node((netID, grade), node_next, node_prev)

        node_prev.next = new_node
        node_next.prev = new_node
        
        

    
