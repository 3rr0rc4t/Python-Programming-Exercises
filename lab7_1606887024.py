import math

class Bola:
    def __init__(self,nama,jariJari):
        self.nama = nama
        self.jarijari = jariJari
    def getLuasPermukaan(self):
        return round((math.pi * 4 * self.jarijari * self.jarijari),2)
    def GetVolume(self):
        return round(((4/3) * math.pi * self.jarijari * self.jarijari * self.jarijari),2)
    def __str__(self):
        string = "==============================================\n"
        string += "Nama saya " + self.nama + '\n'
        string += "Saya adalah Bola\n"
        string += "Saya memiliki\n"
        string += "\t- Jari jari : " + str(self.jarijari) + '\n'
        string += "\t- Luas Permukaan : " + str(Bola.getLuasPermukaan(self)) + '\n'
        string += "\t- Volume : " + str(Bola.GetVolume(self))

        return string

class Tabung:
    def __init__(self,nama,jariJari,tinggi):
        self.nama = nama
        self.jarijari = jariJari
        self.tinggi = tinggi
    def getLuasPermukaan(self):
        return round(2*(self.jarijari*self.jarijari*math.pi) + (self.tinggi * 2 * self.jarijari * math.pi),2)
    def getVolume(self):
        return round(self.tinggi * self.jarijari * self.jarijari * math.pi,2)
    def __str__(self):
        string = "==============================================\n"
        string += "Nama saya " + self.nama + '\n'
        string += "Saya adalah Tabung\n"
        string += "Saya memiliki\n"
        string += "\t- Jari jari : " + str(self.jarijari) + ", dan Tinggi : " + str(self.tinggi) + '\n'
        string += "\t- Luas Permukaan : " + str(Tabung.getLuasPermukaan(self)) + '\n'
        string += "\t- Volume : " + str(Tabung.getVolume(self))

        return string
class Limas:
    def __init__(self,nama,panjangSisiAlas,tinggi,sisiMiring):
        self.nama = nama
        self.panjangalas = panjangSisiAlas
        self.tinggi = tinggi
        self.miring = sisiMiring
    def getLuasPermukaan(self):
        return round((self.panjangalas * self.panjangalas) + 4*self.panjangalas*self.miring/2,2)
    def getVolume(self):
        return round(self.panjangalas * self.panjangalas*self.tinggi/3,2)
    def __str__(self):
        string = "==============================================\n"
        string += "Nama saya " + self.nama + '\n'
        string += "Saya adalah Limas\n"
        string += "Saya memiliki\n"
        string += "\t- Panjang sisi alas : " + str(self.panjangalas) + ", Tinggi : " + str(self.tinggi) + ", Sisi miring : " + str(self.miring) + '\n'
        string += "\t- Luas Permukaan : " + str(Limas.getLuasPermukaan(self)) + '\n'
        string += "\t- Volume : " + str(Limas.getVolume(self)) + '\n'
        string += "=============================================="
        return string

bola = Bola("Bola Kecil",21)
tabung = Tabung("Tabung Minyak",7,20)
limas = Limas("Limas Persegi",10,12,15)
print(bola)
print(tabung)
print(limas)
