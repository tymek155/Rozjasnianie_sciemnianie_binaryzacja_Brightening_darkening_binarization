from PIL import Image
import numpy as np

licz = 0

def save(tab):
    global licz
    photo = Image.fromarray(tab)
    photo.save('Zdjecie'+str(licz)+'.bmp')
    licz+=1
    photo.show()

def rozjasnij_sciemnij(photo, b):
    for i in range(photo.shape[0]):
        for j in range(photo.shape[1]):
            if photo[i][j] + b < 0:
                photo[i][j] = 0
            elif photo[i][j] + b < 255:
                photo[i][j] += b
            else:
                photo[i][j] = 255
    save(photo)
    return photo

def rozjasnij_sciemnij_proc(photo, proc):
    if  abs(proc) < 1 or abs(proc) > 99:
        print("Bledna wartosc procentowa rozjasniania/sciemniania")
        return
    for i in range(photo.shape[0]):
        for j in range(photo.shape[1]):
            if photo[i][j] + round(photo[i][j]*(proc/100)) < 0:
                photo[i][j] = 0
            elif photo[i][j] + round(photo[i][j]*(proc/100)) <255:
                photo[i][j] += round(photo[i][j]*(proc/100))
            else:
                photo[i][j] = 255
    save(photo)
    return photo


def rozjasnij_krokowo(photo):
    opt = True
    while(opt):
        krok = float(input("Podaj wartosc z zakresu 10-20 do rozjasniania krokowego: "))
        if krok >= 10 and krok <= 20:
            opt = False
        else:
            print("Podano wartosc spoza zakresu!")
    for i in range(3):
        photo = rozjasnij_sciemnij_proc(photo, krok)


def binaryzacja(photo, a=127):
    for i in range(photo.shape[0]):
        for j in range(photo.shape[1]):
            if photo[i][j] <= a:
                photo[i][j] = 0
            else:
                photo[i][j] = 255
    save(photo)

def binaryzacja_input(photo):
    opt = True
    while(opt):
        stp = int(input("Podaj wartosc progu binarzyacji 0-255: "))
        if stp >= 0 and stp <= 255:
            opt = False
        else:
            print("Podano wartosc spoza zakresu!")
    binaryzacja(photo, stp)

def main():
    photo = Image.open("Mapa_MD_no_terrain_low_res_Gray.bmp")

    #photo = Image.open("pikachu.jpg")
    #photo = photo.convert("L")
    photo.show()
    photo = np.array(photo)
    #rozjasnij_sciemnij_proc(photo, -50)
    rozjasnij_krokowo(photo)
    #binaryzacja(photo)
    binaryzacja_input(photo)



main()