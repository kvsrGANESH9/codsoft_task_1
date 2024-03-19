    def display():
       if not l:
           print('The to-do list is empty')
       else:
            print('Yhe to-do list: ',l)
def add():
        n=int(input('How many elements you want to insert: '))
        for i in range(0,n):
            u=input('Enter the element: ')
            l.append(u)
        print('The elements are succesfully added')
def remove():
        if not l:
            print('The list is empty')
        else:
            e=input('Enter the element to remove from the list: ')
            if e in l:
                l.remove(e)
                print('The element is removed')
            else:
                print('The element is not found in to-do list')
l=[]
while True:
    i=input('1: display to-do list\n2:add element to to-do list\n3: remove element from to-do list')
    if i=='1':
        display()
    elif i=='2':
        add()
    elif i=='3':
        remove()
    else:
        print('Invalid input has given')
        break
    
    o=input('You want to perform more tasks:\nyes\nNo')
    if o.lower()=='yes':
        continue
    elif o.lower()=='no':
        print('Thankyou')
        break
    else:
        print('Invalid input')
        break
