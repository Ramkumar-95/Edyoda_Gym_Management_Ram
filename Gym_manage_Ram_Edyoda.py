class SuperUser:
    regimens = {}
    members_of_gym = {}

    @classmethod
    def add_member(cls, member):
        SuperUser.members_of_gym[member.get_contactno()] = member


class Member:
    def __init__(self, name, age, gender, contactno, email, bmi, membership):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__contactno = contactno
        self.__email = email
        self.__bmi = bmi
        self.__membership = membership

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_contactno(self):
        return self.__contactno

    def set_contactno(self, contactno):
        self.__contactno = contactno

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_bmi(self):
        return self.__bmi

    def set_bmi(self, bmi):
        self.__bmi = bmi

    def get_membership(self):
        return self.__membership

    def set_membership(self, membership):
        self.__membership = membership



print('Edyoda GYM'.center(50, '-'))
print('-' * 50)

while True:
    print("Enter 1 for User and 2 for SuperUser:")
    print("To Exit Enter 0")
    val = int(input())

    if val == 1:
        print('User'.center(50, "-"))
        while True:
            print('''
                    1=> My Regimen
                    2=> My Profile
                    0=> Exit
                    ''')
            choice = int(input())

            if choice == 1:
                enter_no = int(input("Enter Contact No:"))
                print("Regimen Based on your BMI")
                for i in SuperUser.regimens:
                    if i == enter_no:
                        for j, k in SuperUser.regimens[i].items():
                            print(j, ":", k)

            elif choice == 2:
                enter_no = int(input("Enter Contact No:"))
                try:
                    for i in SuperUser.members_of_gym:
                        if i == enter_no:
                            m = SuperUser.members_of_gym[i]
                            print("Your Profile".center(50, "-"))
                            print(f"Name: {m.get_name()}"
                                  f"\nAge: {m.get_age()}"
                                  f"\nGender: {m.get_gender()}"
                                  f"\nEmail: {m.get_email()}"
                                  f"\nBMI: {m.get_bmi()}"
                                  f"\nMembership Duration: {m.get_membership()}")
                except:
                    print("User Doesn't Exist")

            elif choice == 0:
                break

            else:
                print("Invalid Input")

    elif val == 2:
        print("Super User".center(50, "-"))
        while True:
            print('''
            1=> Create User
            2=> View User
            3=> Delete User
            4=> Update User
            5=> Create Regimen
            6=> View Regimen
            7=> Delete Regimen
            8=> Update Regimen
            0=> Exit
            ''')
            choice = int(input())

            if choice == 1:
                print("Enter User Details\n")
                name = input("Enter Name:")
                age = int(input("Enter Age:"))
                gender = input("Enter Gender:")
                no = int(input("Enter Mobile No.:"))
                email = input("Enter Email:")
                bmi = int(input("Enter BMI:"))
                membership = int(input("Enter Membership Duration In Months:"))

                if bmi < 18.5:
                    r = {'Mon': 'Chest',
                         'Tue': 'Biceps',
                         'Wed': 'Rest',
                         'Thu': 'Back',
                         'Fri': 'Triceps',
                         'Sat': 'Rest',
                         'Sun': 'Rest'
                         }

                elif bmi < 25:
                    r = {'Mon': 'Chest',
                         'Tue': 'Biceps',
                         'Wed': 'Cardio/Abs',
                         'Thu': 'Back',
                         'Fri': 'Triceps',
                         'Sat': 'Legs',
                         'Sun': 'Rest'
                         }

                elif bmi < 30:
                    r = {'Mon': 'Chest',
                         'Tue': 'Biceps',
                         'Wed': 'Abs/Cardio',
                         'Thu': 'Back',
                         'Fri': 'Triceps',
                         'Sat': 'Legs',
                         'Sun': 'Cardio'
                         }

                elif bmi > 30:
                    r = {'Mon': 'Chest',
                         'Tue': 'Biceps',
                         'Wed': 'Cardio',
                         'Thu': 'Back',
                         'Fri': 'Triceps',
                         'Sat': 'Cardio',
                         'Sun': 'Cardio'
                         }

                member = Member(name, age, gender, no, email, bmi, membership)
                SuperUser.regimens[no] = r
                SuperUser.add_member(member)


            elif choice == 2:
                enter_no = int(input("Enter Contact No of User:"))
                for i in SuperUser.members_of_gym:
                    if i == enter_no:
                        m = SuperUser.members_of_gym[i]
                        print(f"Name: {m.get_name()}"
                              f"\nAge: {m.get_age()}"
                              f"\nGender: {m.get_gender()}"
                              f"\nEmail: {m.get_email()}"
                              f"\nBMI: {m.get_bmi()}"
                              f"\nMembership Duration: {m.get_membership()}")
                    else:
                        print("User Doesn't Exist")


            elif choice == 3:
                enter_no = int(input("Enter Contact No of User:"))
                try:
                    for i in SuperUser.members_of_gym:
                        if i == enter_no:
                            SuperUser.members_of_gym.pop(enter_no)
                            print("Sucessfully Deleted User")
                except:
                    print("User doesn't Exist")

            elif choice == 4:
                enter_no = int(input("Enter Contact No of User:"))
                ask = input("Enter if you want to extend or revoke:")
                if ask == 'extend':
                    extend = int(input("Enter for how many do you want to extebd:"))
                    for i in SuperUser.members_of_gym:
                        if i == enter_no:
                            d = member.get_membership()
                            s = d + extend
                            member.set_membership(s)
                            print("Extended Sucessfully")

                elif ask == 'revoke':
                    for i in SuperUser.members_of_gym:
                        if i == enter_no:
                            member.set_membership(0)
                            print("Membership Revoked")

            elif choice == 5:
                enter_no = int(input("Enter Contact No of User:"))
                for i in SuperUser.regimens:
                    if i == enter_no:
                        for j in SuperUser.regimens[i]:
                            SuperUser.regimens[i][j] = input(j + ':')

            elif choice == 6:
                enter_no = int(input("Enter Contact No of User:"))
                for i in SuperUser.regimens:
                    if i == enter_no:
                        for j, k in SuperUser.regimens[i].items():
                            print(j, ':', k)

            elif choice == 7:
                enter_no = int(input("Enter Contact No of User:"))
                for i in SuperUser.regimens:
                    if i == enter_no:
                        SuperUser.regimens.pop(enter_no)
                        print("Regimen Deleted Sucessfully")

            elif choice == 8:
                enter_no = int(input("Enter Contact No of User:"))
                for i in SuperUser.regimens:
                    if i == enter_no:
                        day = input("Enter the day on which you want to update:")
                        for j in SuperUser.regimens[i]:
                            if j == day:
                                SuperUser.regimens[i][j] = input("Enter the Workout:")
                                print("Updated Sucessfully")

            elif choice == 0:
                break

            else:
                print("Invalid Input")

    elif val == 0:
        break

    else:
        print("Invalid Input")
