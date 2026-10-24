class PemainBola :
    def __init__(self, nama, posisi):
        self.nama_pemain = nama
        self.posisi_pemain = posisi
        self.jumlah_gol = 0
        self.stamina = 100
        pass

    def sprint(self):
        if self.stamina < 15 :
            print(f"{self.nama_pemain} terlalu lelah untuk sprint")
        else :
            self.stamina -= 15
            print(f"{self.nama_pemain} melakukan sprint")

    def oper_bola(self, rekan_tim):
        if self.stamina < 1 :
            print(f"{self.nama_pemain} terlalu lelah untuk mengoper")
        else :
            self.stamina -= 1
            print(f"{self.nama_pemain} mengoper bola kepada", rekan_tim.nama_pemain)

    def shooting(self):
        if self.stamina < 20 :
            print(f"{self.nama_pemain} terlalu lelah untuk shooting ke gawang")
        else :
            self.stamina -= 20
            print(f"{self.nama_pemain} melakukan shotting ke gawang dan GOLLL!!")
            self.jumlah_gol += 1

    def info_pemain(self):
        print("-------------------------------------")
        print("Info :", self.nama_pemain)
        print("Posisi :", self.posisi_pemain)
        print("Stamina :", self.stamina)
        print("Jumlah Gol :", self.jumlah_gol)

pemain1 = PemainBola('Neymar', 'Sayap Kiri')
pemain2 = PemainBola('Suarez', 'Striker')
pemain3 = PemainBola('Messi', 'Sayap Kanan')

pemain1.info_pemain()
pemain2.info_pemain()
pemain3.info_pemain()

pemain1.sprint()
pemain1.oper_bola(pemain2)
pemain2.oper_bola(pemain3)
pemain3.sprint()
pemain3.oper_bola(pemain2)
pemain2.shooting()
pemain2.info_pemain()