from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    node = lnk_lst.header.next
    result = DoublyLinkedList()

    
    while node is not None and node != lnk_lst.trailer:
        result.add_last(node.data)
        node = node.next
    return result

    

def deep_copy_linked_list(lnk_lst):
    node = lnk_lst.header.next
    result = DoublyLinkedList()

    while node is not None and node != lnk_lst.trailer:

        if isinstance(node.data, int):
            result.add_last(node.data)
        else:
            result.add_last(deep_copy_linked_list(node.data))

        node = node.next

    return result


    





