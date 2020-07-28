# create a file and let user write
filename = 'guest.txt'
name = input("please give me your name: \n")
with open(filename, 'a') as file_object:
    file_object.write(name)
    file_object.write('\n')
