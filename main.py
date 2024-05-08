
allUsers=[]
allNewUsers =[
    ['ahmad','12','computer science','cairo'], #i(0)
    ['mohammad','12','computer science','cairo'],#i
    ['ali','12','computer science','cairo'],#i
]
while True:
    print("""
          Welcome to Python
          1- add new user
          2- delete user
          3- show all users
          4- show speacifec user
          5- update user data
          6- exit
          """)
    #  convert str to int
    choice = int(input('Enter your choice:'))
    print('you choice is :', choice)
    if choice == 1:
        print('you want to add new user')
        username= input('please inter your username :')
        age = int(input('please inter your age :'))
        major = input('please inter your major :')
        city = input('please inter your city :')
        createduser= [username,age,major,city]

        print(createduser)
        allUsers.append(createduser)
    elif choice == 2:
        print('you want to delete user')
        userToDelete = input ('inter the username')
        for i in allUsers:
            if i[0]== userToDelete:
                allUsers.remove(i) # value or index
                print("user deleted")
    elif choice == 3:
        print('you want to show all users')
        print(allUsers)
    elif choice == 4:
        print('you want to show speacific user')
    elif choice == 5:
        print('update')
        founded=False
        userToUpdate = input('please inter your username to update :')

        for i in allUsers:
            if i[0]== userToUpdate:
                newUsername = input('please inter your new username :')
                i[0]= newUsername
                newAge = int(input('please inter your new age :'))
                i[1]= newAge
                newMajor = input('please inter your new major :')
                i[2]= newMajor
                newCity = input('please inter your new city :')
                i[3]= newCity
                founded=True
        if founded ==False:
            print(('no user founded'))

    elif choice == 6:
        print('you want to exit')
        break
#  task > conver the created user list to dictionary
# example : createduserAslist = ['ahmad','12','computer science','cairo']
# createdUserasDictionary = {'username':'ahmad','age':'12','major':'computer science','city':'cairo'}
# update all the logic to handel the delete,update ,show all users,show speacific user
# as dictionary
