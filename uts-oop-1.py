# 2072025 Sherly Santiadi

class SegiEmpat:
    def __init__(self, panjang, lebar):
        self.__setPanjang(panjang)
        self.__setLebar(lebar)

    def getPanjang(self):
        return self.__panjang
    def __setPanjang(self, panjang):
            self.__panjang = panjang if panjang >= 0 else panjang*-1
    def getLebar(self):
        return self.__lebar
    def __setLebar(self, lebar):
        self.__lebar = lebar if lebar >= 0 else lebar*-1
    
    def hitungLuas(self):
        return self.__panjang*self.__lebar
def main():
    p = SegiEmpat(-10,11)
    print(p.getPanjang())    
    print(p.getLebar())
    luas = p.hitungLuas()
    print(luas)
main()
