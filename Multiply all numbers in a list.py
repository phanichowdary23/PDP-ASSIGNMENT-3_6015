def multiplyList(myList) : 

    # Multiply elements one by one 

    result = 1

    for x in myList: 

         result = result * x  

    return result  
      
# Driver code 

list1 = [1, 3, 5]  
list2 = [2, 4, 6] 
print(multiplyList(list1)) 
print(multiplyList(list2)) 