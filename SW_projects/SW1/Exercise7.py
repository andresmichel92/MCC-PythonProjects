import random
nocaps_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
caps_list = ["A","B","C","D","E","f","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sym_list = ["!","#","$","%","&","/","?","@"]


def get_random(tail):
    ran = random.randint(0, tail-1)
    return ran


def ran_list_value(lista):
    val = lista[get_random(len(lista))]
    return val


def generate_password(size):
    psswrd = []
    i = 0
    j = 0
    k = 0
    num_sym = size - random.randint(2, int(size/2))
    # print(str(num_sym))
    num_nocaps = size - num_sym - 1
    # print(str(num_nocaps))
    num_caps = size - (num_nocaps + num_sym)
    # print(str(num_caps))
    while i < num_sym:
        psswrd.append(ran_list_value(sym_list))
        i = i + 1
    while j < num_nocaps:
        psswrd.append(ran_list_value(nocaps_list))
        j = j + 1
    while k < num_caps:
        psswrd.append(ran_list_value(caps_list))
        k = k + 1

    random.shuffle(psswrd)
    return psswrd


def list_to_str(list1):
    i = 0
    msg = ""
    while i < len(list1):
        msg = msg + str(list1[i])
        i = i + 1
    return msg


size_num = int(input("Introduce password size, greater than 6: "))
contra = generate_password(size_num)
print("Your password is: " + list_to_str(contra))


