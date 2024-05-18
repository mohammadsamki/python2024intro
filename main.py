
# allUsers=[]
# allNewUsers =[
#     ['ahmad','12','computer science','cairo'], #i(0)
#     ['mohammad','12','computer science','cairo'],#i
#     ['ali','12','computer science','cairo'],#i
# ]
# # test1 = {"name":'ahmad',"age":20}
# def addUser():
#         print('you want to add new user')
#         username= input('please inter your username :')
#         age = int(input('please inter your age :'))
#         major = input('please inter your major :')
#         city = input('please inter your city :')
#         skillsNumer = int(input('inter your skills num'))
#         skills={}
#         for i in range(skillsNumer):
#             skill = input(f'inter skill num {i +1} ')
#             skills[f'skiil{i+1}']=skill

#         createduser= {
#             "username":username,
#             "age":age,
#             "major":major,
#             "city":city,
#             "skills":skills
#         }
#         print(createduser)
#         allUsers.append(createduser)
#         return createduser
# def deletUser():
#         print('you want to delete user')
#         userToDelete = input ('inter the username')
#         for i in allUsers:
#             if i['username']== userToDelete:
#                 allUsers.remove(i) # value or index
#                 print("user deleted")
# def showCurrentUser():
#         print('you want to show speacific user')
#         userToShow = input('inter the username')
#         isExisted=False
#         for i in allUsers:
#             if i['username'] == userToShow:
#                 print(i)
#                 isExisted=True
#         if isExisted ==False:
#             print('no user found ')
# def updateUser():
#         print('update')
#         founded=False
#         userToUpdate = input('please inter your username to update :')

#         for i in allUsers:
#             if i['username']== userToUpdate:
#                 newUsername = input('please inter your new username :')
#                 i['username']= newUsername
#                 newAge = int(input('please inter your new age :'))
#                 i['age']= newAge
#                 newMajor = input('please inter your new major :')
#                 i['major']= newMajor
#                 newCity = input('please inter your new city :')
#                 i['city']= newCity
#                 founded=True
#         if founded ==False:
#             print(('no user founded'))

# while True:
#     print("""
#           Welcome to Python
#           1- add new user
#           2- delete user
#           3- show all users
#           4- show speacifec user
#           5- update user data
#           6- exit
#           """)
#     #  convert str to int
#     choice = int(input('Enter your choice:'))
#     print('you choice is :', choice)
#     if choice == 1:
#         addUser()


#     elif choice == 2:
#         deletUser()
#     elif choice == 3:
#         print('you want to show all users')
#         print(allUsers)
#     elif choice == 4:

#         showCurrentUser()
#     elif choice == 5:
#        updateUser()
#     elif choice == 6:
#         print('you want to exit')
#         break

# #  task > conver the created user list to dictionary
# # example : createduserAslist = ['ahmad','12','computer science','cairo']
# # createdUserasDictionary = {'username':'ahmad','age':'12','major':'computer science','city':'cairo'}
# # update all the logic to handel the delete,update ,show all users,show speacific user
# # as dictionary


# # task 11/5 :
# # add new field called skills :>
# # ask the user to inter the skills number
# # initer the skills
# # [skill1,skill2]
# # user={
#     # "username": "ahmad",
#     # "age":26,
#     #  "major": 'IT",
#     #  "city": "irbid",
#     #  inter you skills number > 3
#     #  list skills = []
#     # input skill 1
#     # skills.append(skill1)
#     # input skill 2
#     #  skills.append(skill2)
#     # input skill 3
#     #  skills.append(skill3)

#     #  "skills": skills
# # }
# print(f"""
#     [ , , ,]
#     [ , , ,]
#     [ , , ,]

#       """)
player1=''
player2=''

bord=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
replaced=[]
def printBord():
    for i in bord:
        print(i)

def replaceIndex(player):
    choice = int(input('select the place'))
    if choice <1 or choice>9:
        print('select valid input ')
        return 'select valid input '
    for i in replaced:
        if i ==choice:
            print("allready selected")
            return "allready selected"
    # li1[0]='x'
    if (choice / 3) <= 1:
        print('you are in the first row ')
        print(f"you are in the index {choice-1}")
        bord[0][choice-1]=player
    elif (choice / 3) <= 2:
        print('you are in the sec row')
        print(f"you are in the index {choice-4}")
        bord[1][choice-4]=player


    elif (choice / 3) <= 3:
        print('you are in the therd row')
        print(f"you are in the index {choice-7}")
        bord[2][choice-7]=player
    replaced.append(choice)
player1 = input('chose x or o')
if player1 == 'x':
    player2 ='o'
else:
    player2 ='x'
turn = 1
while True:
    if turn % 2 ==0:
        replaceIndex(player2)
    else:
        replaceIndex(player1)

    printBord()
    turn+=1

