""" Kelcy Gooch: kjg116
    Clayton Hudspeth: ch1518
    Class section 1
    Lab section 4
"""
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

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.front == None:
            self.front = ListNode(value)
            self.rear = self.front
        else:
            self.rear.set_link(ListNode(value))
            self.rear = self.rear.get_link()


    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Cannot dequeue from an empty queue.")
        value = self.front.get_item()
        self.front = self.front.get_link()
        if self.front == None:
            self.rear = None
        return value


    def destroy(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None:
            return True
        return False

    def is_full(self):
        return False

    def front(self):
        if self.is_empty():
            raise RuntimeError("Cannot get first item from an empty queue.")
        return self.front.get_item()

    def __len__(self):
        total = 0
        temp = self.front

        while temp != None:
            total += 1
            temp = temp.get_link()

        return total

    def __str__(self):
        a_string = "["
        temp = self.front

        while temp != None:
            a_string += str(temp.get_item())
            a_string += ', '
            temp = temp.get_link()

        a_string = a_string.strip(', ')
        a_string += ']'
        return a_string

def main():

    #Recieves input from user
    lanes = int(input("Number of check-out lines to be opened: "))
    customers = open("customers.txt", "r")
    queues = []

    #appends number of queues to list
    for items in range(lanes):
        queues.append(Queue())

    #places customers in line
    for customer in customers:
        customer = customer.strip()
        count = 0
        length_list =[]
        for each in queues:
            count += 1
            length_list.append(len(queues[count-1]))
        index = length_list.index(min(length_list))
        queues[index].enqueue(int(customer))

    #calculates the average time in each line
    lists = []
    for i in range(len(queues)):
        time_list = [0]
        time = 0
        while queues[i].is_empty() is False and len(queues[i]) != 1:
            value = queues[i].dequeue()
            time += value + 1
            time_list.append(time)
        lists.append(time_list)

    #calculates the total average wait time
    averages = []
    for i in range(len(queues)):
        sum = 0
        people = 0
        for each in lists[i]:
            sum += each
            people += 1
        average = sum/people
        averages.append(average)

    total_time = 0
    for i in averages:
        total_time += i

    total_average = total_time / len(averages)
    print(format(total_average, '.2f'))
main()