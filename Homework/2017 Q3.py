from DoublyLinkedList import DoublyLinkedList   


def insert_sorted(srt_lnk_lst, elem):
    node = srt_lnk_lst.header.next
    replace = False

    if node is srt_lnk_lst.trailer or elem < node.data:
        new = srt_lnk_lst.Node(elem)
        new.prev = srt_lnk_lst.header
        new.next = node
        node.prev = node
        srt_lnk_lst.header.next = new
        return srt_lnk_lst

    while node is not srt_lnk_lst.trailer:
        if not replace and node.data < elem:
            new = DoublyLinkedList.Node(elem)
            new.prev = node.prev
            new.next = node
            node.prev = new
            node.prev.next = new
            replace = True
        node = node.next

    if replace == False:
        node = srt_lnk_lst.trailer.prev
        new = DoublyLinkedList().Node(elem)
        new.prev = node
        new.next = srt_lnk_lst.trailer
        node.next = new
        srt_lnk_lst.trailer.prev = new
    return srt_lnk_lst


            





