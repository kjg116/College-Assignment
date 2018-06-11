#Kelcy Gooch
#Class Section 1
#CSE 1384
#Lab 6 - Sum of nested list


def sum(n):
    total = 0
    for items in n:
        if isinstance(items, list):
            total+=sum(items)
        else:
            total+=items
    return total

list1 = str([1,[2,3]])
list2 = str([4,[5,6],[7,[8,9]]])
list3 = str([9,[8,[7,[6,[5]]]]])
list4 = str([[12,[[],[]],5],[3,[[11,[8,10]]],[9,4,6]],1,[[[2]]],0,7])

print("List:",list1)
print("The sum of the values is", sum([1,[2,3]]))
print('')
print("List:",list2)
print('')
print("The sum of the values is", sum([4,[5,6],[7,[8,9]]]))
print('')
print("List:",list3)
print("The sum of the values is", sum([9,[8,[7,[6,[5]]]]]))
print('')
print("List:",list4)
print("The sum of the values is", sum([[12,[[],[]],5],[3,[[11,[8,10]]],[9,4,6]],1,[[[2]]],0,7]))
