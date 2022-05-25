'''
funktionen Python
Max.Eberwein
'''
import random

a_list = []
def check_input(a_list, ui):
    if ui < 0 or ui > 10:
        return False
    if ui in a_list:

    if ui.isnumeric:
        ui = int(ui)
        else:
            print("Die Zahl ist nicht Numaric, nocheinmal eingeben")
        return False
    return True


for x in range(10):

        if ui.isnumeric:
            ui = int(ui)
        else:
            print("Die Zahl ist nicht Numaric, nocheinmal eingeben")


    if (check_input(a_list, ui) == False):
        print("Bitte nocheinmal eingeben")
        continue
    else:
        a_list.append(ui)
        print(a_list)