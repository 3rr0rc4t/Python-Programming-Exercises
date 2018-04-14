#Tugas 2 Kelas DDP1 Eksternal
#Athina Maria Angelica (1606887024)

from tkinter import *
#from PIL import Image, ImageTk

#Define variables
digits = ["nol","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan"]
size = 50
dash = "-"*size
i = 0

class Drink:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return self.name

#drinks list being read from file
dataStream = open("Tugas2_Athina_Maria_Angelica_1606887024.txt","r+")
drinks = []

for line in dataStream:
    stuff = line.rstrip('\r\n').split(',')
    stuff = [stuff.strip() for stuff in stuff]
    instr = Drink(stuff[0],int(stuff[2]),int(stuff[1]))
    drinks.append(instr)

#Make window

class vending_machine(Tk):

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        #impath = "Equil.png"
        #self.img = PhotoImage(file=impath)

    def initialize(self):

        self.grid
        self.labelVariable = StringVar()
        self.labelVariable.set("Choose a drink\n")
        label = Label(self,textvariable = self.labelVariable)
        self.makeButtons()
        label.grid(column = 0, row = 0, columnspan = 2, rowspan=2)

    def makeButtons(self):
        # ----------------------------------------------
        # inisiasi list untuk menampung setiap variable yang akan di assign ke setiap button
        # jika tidak dalam bentuk list maka tiap button akan mendapatkan text yang sama
        # harus disimpan ke dalam variable global agar dapat diakses pada class vending machine
        self.disp = []
        # ----------------------------------------------
        #self.img = PhotoImage(file="Equil.png")

        impath = r"Equil.gif"
        img = PhotoImage(file=impath)

        button9 = Button(self, image=img)
        print("OK")

        for i in range(0,len(drinks)):
            # ----------------------------------------------
            self.disp.append(StringVar())
            self.disp[i].set(drinks[i].name + '\nRp ' +str(drinks[i].price)+"\nStok: "+str(drinks[i].stock))
            textInButton = drinks[i].name + '\nRp ' + str(drinks[i].price) + "\nStok: " + str(drinks[i].stock)
            # ----------------------------------------------

            #impath = "D:\Python\Tugas2_Athina_Maria_Angelica_1606887024" +'\\'+ drinks[i].name + ".png"

            impath = "Equil.gif"
            self.img = PhotoImage(file=impath)

            # ----------------------------------------------
            button = Button(self, image=self.img, textvariable=self.disp[i],text = textInButton, padx = 10, command = lambda i = i : self.onClick(i))
            # ----------------------------------------------

            #button.image = image
            if i % 2 == 0:
                button.grid(row = i+2, column = 0)
            else:
                button.grid(row = i+1, column = 1)
            button.configure()

        admin = Button(self, text="Admin Menu", command = self.adminMenu)
        admin.grid(row = i+2, column = 1)
        self.update()



    def onClick(self,i):
        if drinks[i].stock > 0:
            drinks[i].stock -= 1
            # ----------------------------------------------
            # Gunakan variable yang ada di "textvariable" karena variabel ini yang akan dikenal oleh tiap button
            self.disp[i].set(str(drinks[i].name)+"\nharga: "+
                             str(drinks[i].price)+"\n stock : "+
                             str(drinks[i].stock))
            # ----------------------------------------------
            print(drinks[i].name," stock : ",drinks[i].stock)

            # ----------------------------------------------
            # bagian yang ini udah bener, kenapa gak diaplikasikan ke button?? :D
            # ----------------------------------------------
            self.labelVariable.set("You chose "+drinks[i].name+" for "+spell(str(drinks[i].price)))
            clear(dataStream)
            save()

    def adminMenu(self):
        print("Admin menu")
        win = Tk()
        win.title("Admin Menu")
        win.grid
        stock = Button(win, text = "Tambah stok", command = self.addStock)
        stock.grid(row = 0, column = 0)
        boi = Button(win, text = "Ubah harga", command = self.addStock)
        boi.grid(row = 1, column = 0)
        wtf = Button(win, text = "Tambah barang", command = self.addStock)
        wtf.grid(row = 2, column = 0)
        exit = Button(win, text = "Return", command = self.restart)
        exit.grid(row = 3, column = 0)
        win.mainloop()

    def restart(self):
        print("go back")
        win2 = vending_machine(None)

    def addStock(self):
        print("ganti stok")

#Define functions

def menu():
    print("\nSelamat datang, silahkan pilih minuman".center(size))
    print(dash)
    print()
    print("{:<30s}{:<20s}{:<6s}".format("Minuman","Harga","Stok"))
    for x in range (0,len(drinks)):
        print(x+1,".","{:<24s}".format(drinks[x].name),"{:<1s}".format("Rp"),"{:>11d}".format(drinks[x].price),"{:<3}".format(" "),"{:>5d}".format(drinks[x].stock))
    print()
    userint = input("Ketik angka pilihan anda: ")
    if(userint == 'admin'):
        password = input("Masukkan password: ")
        if (password == "1606887024"):
            adminmenu()
        else:
            print("Password salah")
    elif(0<int(userint)<=len(drinks)):
        if(int(drinks[int(userint)-1].stock)>0):
            print("Anda memilih",drinks[int(userint)-1].name,"dengan harga",spell(str(drinks[int(userint)-1].price)),"rupiah,")
            print("Terima kasih")
            drinks[int(userint)-1].stock = drinks[int(userint)-1].stock - 1
            clear(dataStream)
            save()
        else:
            print("Maaf, stok minuman habis. Mohon pilih minuman lain.")

def adminmenu(): #TODO
    print("\nMenu Maintenance".center(size))
"""    print(dash)
    print()
    print("1. Tambah stok")
    print("2. Tambah jenis barang")
    print("3. Ubah harga")
    print("4. Kembali ke awal")
    print()
    userint = input("Pilih perintah: ")
    if(userint == '1'):
        addstock()
    if(userint == '2'):
        addtype()
    if(userint == '3'):
        changeprice()
    if(userint == '4'):
        menu()
    else:
        adminmenu()

def addstock(): #TODO
    print("Stok sekarang")
    print()
    print("{:<25s}{:<6s}".format("Minuman","Stok"))
    for x in range (0,len(drinks)):
        print(x+1,".","{:<24s}".format(drinks[x]["drinkName"]),"{:<3}".format(" "),"{:>6s}".format(drinks[x]["stock"]))
    print()
    addto = int(input("Pilih angka produk: ")) -1
    ask = "Banyak "+drinks[addto]["drinkName"]+" yang ingin ditambahkan: "
    addamt = int(input(ask))
    amt2add = int(drinks[addto]["stock"])
    add = int(addamt)
    amt2add = amt2add + addamt
    drinks[addto]["stock"] = str(amt2add)
    clear(dataStream)
    save()

def addtype(): #TODO
    newtype = input("Nama produk: ")
    newprice = input("Harga produk: ")
    newamt = input("Stok produk: ")
    if(len(newprice) <= 6):
        drinks2add = {"drinkName":newtype,"stock":newamt,"price":newprice}
        drinks.append(drinks2add)
    else:
        print("Harga melebihi batas maksimal")
    clear(dataStream)
    save()

def changeprice():
    print("Daftar Harga")
    for x in range (0,len(drinks)):
        print(x+1,".","{:<24s}".format(drinks[x]["drinkName"]),"{:<1s}".format("Rp"),"{:>11s}".format(drinks[x]["price"]))
    print()
    whichprice = int(input("Pilih angka produk: ")) - 1
    newprice = input("Harga baru: ")
    if(len(newprice) <= 6):
        drinks[whichprice]["price"] = newprice
    else:
        print("Harga melebihi batas maksimal")
    clear(dataStream)
    save()
"""
def onedgt(dgt):
    return digits[int(dgt)]

def twodgt(dgt):
    if(dgt[0]=='0'):
        if(dgt[1]=='0'):
            return ''
        else:
            return onedgt(dgt)
    elif(dgt[0]=='1'):
        if(dgt[1]=='0'):
            return "sepuluh"
        elif(dgt[1]=='1'):
            return "sebelas"
        else:
            return onedgt(dgt[1])+" belas"
    else:
        if(dgt[1] == '0'):
            return onedgt(dgt[0])+" puluh"
        else:
            return onedgt(dgt[0])+" puluh "+onedgt(dgt[1])

def threedgt(dgt):
    if(dgt[0] == '0'):
        return twodgt(dgt[1:3])
    elif(dgt[0] == '1'):
        return "seratus "+twodgt(dgt[1:3])
    else:
        return onedgt(dgt[0])+" ratus "+twodgt(dgt[1:3])

def fourdgt(dgt):
    if(dgt[0] == '0'):
        return threedgt(dgt[1:4])
    elif(dgt[0]=='1'):
        return "seribu "+threedgt(dgt[1:4])
    else:
        return onedgt(dgt[0])+" ribu "+threedgt(dgt[1:4])

def fivedgt(dgt):
    return twodgt(dgt[0:2])+" ribu "+threedgt(dgt[2:5])

def sixdgt(dgt):
    return threedgt(dgt[0:3])+" ribu "+threedgt(dgt[3:6])

def spell(dgt):
    if(len(dgt) == 2):
        return twodgt(dgt)
    elif(len(dgt) == 1):
        return onedgt(dgt)
    elif(len(dgt) == 3):
        return threedgt(dgt)
    elif(len(dgt) == 4):
        return fourdgt(dgt)
    elif(len(dgt) == 5):
        return fivedgt(dgt)
    elif(len(dgt) == 6):
        return sixdgt(dgt)

def clear(thing):
    #clear file contents to prepare it for saving current drinks list
    thing.seek(0)
    thing.truncate()

def save():
    #write content of drinks to file in format: [drinkName],[price],[stock]
    for x in range(0,len(drinks)):
        line = drinks[x].name+','+str(drinks[x].stock)+','+str(drinks[x].price)+'\n'
        dataStream.write(line)

#Call Functions
print("length of drinks: "+str(len(drinks)))
for i in range(0,len(drinks)):
    print(str(drinks[i].price))
#menu()

app = vending_machine(None)
app.title("Vending Machine")
app.mainloop()

#while(True):
"""
try:
    menu()
except ValueError:
    pass
except KeyboardInterrupt:
    print("\n\nTerima kasih atas transaksi anda")
    dataStream.close()
"""
