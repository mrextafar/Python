import singly_linked_list_ai_test as sllAI
import SinglyLinkedList as sll

# aiList = sllAI.SinglyLinkedList()
# for i in range(10):
#     aiList.append(i)
# aiList.display()



myList = sll.SinglyLinkedList()
for i in range(10):
    myList.append(i)
print(myList.display())
myList.removeByData(5)
print(myList.display())
