#Kelcy Gooch
#Section 1
#CSE 1384

class ListNode:
    def __init__(self, item = None, link = None):
        self.item = item
        self.link = link

    def set_item(self, item):
        self.item = item

    def set_link(self, link):
        self.link = link

    def get_link(self):
        return self.link

    def get_item(self):
        return self.item

class LinkedList(ListNode):

    def __init__(self):
        self.head = None

    def insert_front(self, item):
        if self.head == None:
            self.head = ListNode()
            temp = ListNode(item)
            self.head.set_link(temp)
        else:
            temp = ListNode(item, self.head.get_link())
            self.head.set_link(temp)

    def insert_position(self, item, position):
        if position == 0:
            self.insert_front(item)
        else:
            end = self.head
            temp = end.get_link()
            counter = 0

            while temp != "None":

                if position == counter:
                    newLink = ListNode(item)
                    end.set_link(newLink)
                    newLink.set_link(temp)
                    break
                else:
                    end = temp

                temp = temp.get_link()
                counter += 1

    def insert_end(self, item):
        if self.head is None:
            self.head = ListNode()

        temp = self.head

        while temp.get_link() is not None:
            temp = temp.get_link()

        end = ListNode(item)
        temp.set_link(end)

    def delete_front(self):
        if self.head is None:
            return None
        self.head = self.head.get_link()

    def delete_end(self):
        head = self.head
        temp = head
        while head is not None:
            head.get_link()
        temp.set_link(head)

    def delete_item(self, item):

        end = self.head
        temp = end.get_link()

        while temp != "None":

            if temp.get_item() == item:
                end.set_link(temp.get_link())
                break
            else:
                end = temp
                temp = temp.get_link()


    def delete_list(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "None"
        head = self.head
        list = []
        head = head.get_link()
        while head is not None:
            list.append(head.get_item())
            head = head.get_link()
        return str(list)[1:-1]

    def __repr__(self):
        if self.head is None:
            return "None"
        head = self.head
        list = []
        head = head.get_link()
        while head is not None:
            list.append(head.get_item())
            head = head.get_link()
        return str((list)[1:-1])



