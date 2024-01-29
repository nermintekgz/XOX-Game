class Tablo:
    def __init__(self):
        self.tablo = [[' ' for i in range(3)] for i in range(3)]

    def tablonun_detaylari(self):
        for dikey in self.tablo:
            print('|'.join(dikey))
            print('-' * 5)

    def hamle_yapma(self, yatay, dikey, oyuncu):
        if self.tablo[yatay][dikey] == ' ':
            self.tablo[yatay][dikey] = oyuncu
            return True
        else:
            print('Bu alan dolu. Lütfen boş bir bölme seçiniz.')
            return False

    def kazanma_durumu(self, oyuncu):
        if (self.tablo[0][0] == self.tablo[0][1] == self.tablo[0][2] == oyuncu) or \
                (self.tablo[1][0] == self.tablo[1][1] == self.tablo[1][2] == oyuncu) or \
                (self.tablo[2][0] == self.tablo[2][1] == self.tablo[2][2] == oyuncu) or \
                (self.tablo[0][0] == self.tablo[1][0] == self.tablo[2][0] == oyuncu) or \
                (self.tablo[0][1] == self.tablo[1][1] == self.tablo[2][1] == oyuncu) or \
                (self.tablo[0][2] == self.tablo[1][2] == self.tablo[2][2] == oyuncu) or \
                (self.tablo[0][0] == self.tablo[1][1] == self.tablo[2][2] == oyuncu) or \
                (self.tablo[0][2] == self.tablo[1][1] == self.tablo[2][0] == oyuncu):
            return True

        return False


class Oyun(Tablo):
    def __init__(self):
        super().__init__()
        self.oyuncu_X = input('X kullanıcısının adı: ')
        self.oyuncu_O = input('O kullanıcısının adı: ')
        self.aktif_oyuncu = 'X'

    def kullanici_degisikligi(self):
        if self.aktif_oyuncu == 'X':
            self.aktif_oyuncu = 'O'
        else:
            self.aktif_oyuncu = 'X'

    def oyuncu_hamlesi(self):
        while True:
            self.tablonun_detaylari()
            yatay = int(input(f'{self.aktif_oyuncu} Yatay için hamle seçiniz. (0, 1, 2): '))
            dikey = int(input(f'{self.aktif_oyuncu} Dikey için hamle seçiniz. (0, 1, 2): '))

            if self.hamle_yapma(yatay, dikey, self.aktif_oyuncu):
                if self.kazanma_durumu(self.aktif_oyuncu):
                    self.tablonun_detaylari()
                    if self.aktif_oyuncu == "X":
                        kazanan_oyuncu = self.oyuncu_X
                    else:
                        kazanan_oyuncu = self.oyuncu_O
                    print(f'{self.aktif_oyuncu} adlı oyuncu {kazanan_oyuncu} kazandı.')
                    break
                elif all(hucre != ' ' for dikey in self.tablo for hucre in dikey):
                    self.tablonun_detaylari()
                    print("Oyun berabere bitti.")
                    break
                else:
                    self.kullanici_degisikligi()


xox_oyunu = Oyun()
xox_oyunu.oyuncu_hamlesi()
