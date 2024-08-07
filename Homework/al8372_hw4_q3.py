from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    result = DoublyLinkedList()
    node1 = srt_lnk_lst1.header.next
    node2 = srt_lnk_lst2.header.next
    def merge_sublists(node1, node2):

        if (node1 == srt_lnk_lst1.trailer) and (node2 == srt_lnk_lst2.trailer):
            return result
        
        elif (node1 == srt_lnk_lst1.trailer):
            while node2 != srt_lnk_lst2.trailer:
                result.add_last(node2.data)
                node2 = node2.next
            return result
        
        elif (node2 == srt_lnk_lst2.trailer):
            while node1 != srt_lnk_lst1.trailer:
                result.add_last(node1.data)
                node1 = node1.next
            return result
        
        else:

            if (node1.data < node2.data):
                result.add_last(node1.data)
                return merge_sublists(node1.next, node2)
            
            elif node1.data > node2.data:
                result.add_last(node2.data)
                return merge_sublists(node1, node2.next)

            elif node1.data == node2.data:
                result.add_last(node1.data)
                result.add_last(node2.data)
                return merge_sublists(node1.next, node2.next)

            
    return merge_sublists(node1, node2)

    
