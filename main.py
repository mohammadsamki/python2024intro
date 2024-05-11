
allUsers=[]
allNewUsers =[
    ['ahmad','12','computer science','cairo'], #i(0)
    ['mohammad','12','computer science','cairo'],#i
    ['ali','12','computer science','cairo'],#i
]
# test1 = {"name":'ahmad',"age":20}
def addUser():
        print('you want to add new user')
        username= input('please inter your username :')
        age = int(input('please inter your age :'))
        major = input('please inter your major :')
        city = input('please inter your city :')
        createduser= {
            "username":username,
            "age":age,
            "major":major,
            "city":city
        }
        print(createduser)
        allUsers.append(createduser)
        return createduser
def deletUser():
        print('you want to delete user')
        userToDelete = input ('inter the username')
        for i in allUsers:
            if i['username']== userToDelete:
                allUsers.remove(i) # value or index
                print("user deleted")
def showCurrentUser():
        print('you want to show speacific user')
        userToShow = input('inter the username')
        isExisted=False
        for i in allUsers:
            if i['username'] == userToShow:
                print(i)
                isExisted=True
        if isExisted ==False:
            print('no user found ')
def updateUser():
        print('update')
        founded=False
        userToUpdate = input('please inter your username to update :')

        for i in allUsers:
            if i['username']== userToUpdate:
                newUsername = input('please inter your new username :')
                i['username']= newUsername
                newAge = int(input('please inter your new age :'))
                i['age']= newAge
                newMajor = input('please inter your new major :')
                i['major']= newMajor
                newCity = input('please inter your new city :')
                i['city']= newCity
                founded=True
        if founded ==False:
            print(('no user founded'))

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
        addUser()


    elif choice == 2:
        deletUser()
    elif choice == 3:
        print('you want to show all users')
        print(allUsers)
    elif choice == 4:

        showCurrentUser()
    elif choice == 5:
       updateUser()
    elif choice == 6:
        print('you want to exit')
        break

#  task > conver the created user list to dictionary
# example : createduserAslist = ['ahmad','12','computer science','cairo']
# createdUserasDictionary = {'username':'ahmad','age':'12','major':'computer science','city':'cairo'}
# update all the logic to handel the delete,update ,show all users,show speacific user
# as dictionary


# task 11/5 :
# add new field called skills :>
# ask the user to inter the skills number
# initer the skills
# [skill1,skill2]
# user={
    # "username": "ahmad",
    # "age":26,
    #  "major": 'IT",
    #  "city": "irbid",
    #  "skills": [skill1,skill2]
# }
