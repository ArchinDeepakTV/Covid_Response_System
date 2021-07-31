import time

from Clearing import clear


def Input():
    name = input('Enter Name of Kin : ')
    flag = 0
    while flag == 0:
        email = input('Enter Google Mail ID of Kin : ')

        if email[len(email) - 1] == 'm' and email[len(email) - 2] == 'o' and email[len(email) - 3] == 'c' and \
                email[len(email) - 4] == '.' and email[len(email) - 5] == 'l' and email[len(email) - 6] == 'i' and \
                email[len(email) - 7] == 'a' and email[len(email) - 8] == 'm' and email[len(email) - 9] == 'g' and \
                email[len(email) - 10] == '@':
            flag = 1
        else:
            time.sleep(1)
            clear()
            print('Enter Name of Kin : ' + name)
    return name, email


def Input_User():
    name = input('Enter Name of User : ')
    flag = 0
    while flag == 0:
        email = input('Enter Google Mail ID of User : ')

        if email[len(email) - 1] == 'm' and email[len(email) - 2] == 'o' and email[len(email) - 3] == 'c' and \
                email[len(email) - 4] == '.' and email[len(email) - 5] == 'l' and email[len(email) - 6] == 'i' and \
                email[len(email) - 7] == 'a' and email[len(email) - 8] == 'm' and email[len(email) - 9] == 'g' and \
                email[len(email) - 10] == '@':
            flag = 1
        else:
            time.sleep(1)
            clear()
            print('Enter Name of User : ' + name)
    return name, email


def write_contacts(filename):
    name, email = Input()
    L = [name, " ", email, "\n"]
    File = open(filename, 'a', encoding='utf-8')
    File.writelines(L)
    File.close()


def write_user(filename):
    name, email = Input_User()
    File = open(filename, 'a', encoding='utf-8')
    File.write(name + " " + email + "\n")
    File.close()


if __name__ == '__main__':
    write_contacts('write_contacts.txt')
    write_user('write_user.txt')
