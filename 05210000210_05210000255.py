# Tahtada kaç sütun ve kaç satır olduğunun belirlenmesi için kullanıcıdan sayı alınmasını sağlayan fonksiyon

def sayi_al():
    flag = True
    sayi = input("Satır ve Sütun sayısını giriniz: ")

    while flag:
        try:
            while not 4 <= int(sayi) <= 8:
                sayi = input("Satır ve Sutün sayısını giriniz: ")
            flag = False

        except ValueError:
            sayi = input("Satır ve Sutün sayısını giriniz: ")

    return int(sayi)


# Kullanıcıdan satır ve sütun sayısı alındıktan sonra tahtanın oluşturulmasını sağlayan fonksiyon

def liste_olustur(sayi, oyuncu1, rakip1):
    tahta = [[" " for x in range(sayi)] for i in range(sayi)]

    for x in range(sayi):
        tahta[0][x] = oyuncu1
        tahta[sayi - 1][x] = rakip1

    return tahta


# Taşların hareketini sağlayan fonksiyon

def hareket(sira, sayi, tahta, rakip1, oyuncu1, harf):
    # Oyunda kullanılacak harflerin listesi

    harf_liste = ["A", "B", "C", "D", "E", "F", "G", "H"]
    harf_liste = harf_liste[:sayi]

    # Kullanıcıdan hareket ettireceği taşın bulunduğu konumu ve hareket ettireceği konumunu alan fonksiyon

    def konum_al(rakip, oyuncu, harf):

        # Oyuncunun ve rakibinin belirlenmesi

        if sira % 2 == 0:
            rakip1 = rakip
            oyuncu1 = oyuncu
        else:
            rakip1 = oyuncu
            oyuncu1 = rakip

        flag = True
        while flag:
            try:
                # Sıranın kimde olduğunun yazdırılması

                print(f"Sıra {oyuncu1}")
                tmp = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                tmp = tmp[:sayi]
                # Hareket ettirilecek taşın eski ve yeni konumunun alınması

                konum = input("Eski ve yeni konumu giriniz")
                while len(konum) != 5 or konum[0] not in tmp or konum[1] not in harf or konum[2] != " " \
                        or konum[3] not in tmp or konum[4] not in harf:
                    konum = input("Eski ve yeni konumu giriniz")
                eski_konum = konum.split()[0]
                yeni_konum = konum.split()[1]

                eski_konum = [int(eski_konum[0]) - 1, harf_liste.index(eski_konum[1].upper())]
                yeni_konum = [int(yeni_konum[0]) - 1, harf_liste.index(yeni_konum[1].upper())]

                if tahta[eski_konum[0]][eski_konum[1]] != oyuncu1:
                    continue

                if tahta[yeni_konum[0]][yeni_konum[1]] != " ":
                    continue

                if yeni_konum[0] == eski_konum[0] and yeni_konum[1] == eski_konum[1]:
                    continue

                elif yeni_konum[0] != eski_konum[0] and yeni_konum[1] != eski_konum[1]:
                    continue

                elif yeni_konum[0] == eski_konum[0]:
                    kontrol = True
                    if yeni_konum[1] < eski_konum[1]:
                        adim = -1
                    else:
                        adim = 1
                    for x in range(eski_konum[1], yeni_konum[1] + 1):
                        if tahta[yeni_konum[0]][x] == rakip1:
                            kontrol = False
                    if kontrol:
                        tahta[eski_konum[0]][eski_konum[1]] = " "
                        tahta[yeni_konum[0]][yeni_konum[1]] = oyuncu1
                        flag = False

                elif yeni_konum[1] == eski_konum[1]:
                    kontrol = True
                    if yeni_konum[0] < eski_konum[0]:
                        adim = -1
                        a = yeni_konum[0] - 1
                    else:
                        adim = 1
                        a = yeni_konum[0] + 1
                    for x in range(eski_konum[0], a, adim):
                        if tahta[x][eski_konum[1]] == rakip1:
                            kontrol = False
                    if kontrol:
                        tahta[eski_konum[0]][eski_konum[1]] = " "
                        tahta[yeni_konum[0]][yeni_konum[1]] = oyuncu1
                        flag = False

            except IndexError:
                pass
            except ValueError:
                pass
            except UnboundLocalError:
                pass
            return yeni_konum

    tas = konum_al(rakip1, oyuncu1, harf)
    return tas


# Taşların kilitleyen fonksiyon

def kilit(tas, rakip, oyuncu, tahta, sayi, sira):
    if sira % 2 == 0:
        rakip1 = rakip
        oyuncu1 = oyuncu
    else:
        rakip1 = oyuncu
        oyuncu1 = rakip

    # Köşede bulunmayan taşların kilitlenmesi

    # Taşın solundaki taşların kontrol edilip rakip taşın kilitlenip kilitlenmediğini kontrol edilmesi

    try:
        tas_sol = [tas[0], tas[1] - 1]
        if tahta[tas_sol[0]][tas_sol[1]] == rakip1:
            if tahta[tas_sol[0]][tas_sol[1] - 1] == oyuncu1:
                tahta[tas_sol[0]][tas_sol[1]] = " "
    except IndexError:
        pass

    # Taşın sağındaki taşların kontrol edilip rakip taşın kilitlenip kilitlenmediğini kontrol edilmesi

    try:
        tas_sag = [tas[0], tas[1] + 1]
        if tahta[tas_sag[0]][tas_sag[1]] == rakip1:
            if tahta[tas_sag[0]][tas_sag[1] + 1] == oyuncu1:
                tahta[tas_sag[0]][tas_sag[1]] = " "
    except IndexError:
        pass

    # Taşın aşağısındaki taşların kontrol edilip rakip taşın kilitlenip kilitlenmediğini kontrol edilmesi

    try:
        tas_asagi = [tas[0] + 1, tas[1]]
        if tahta[tas_asagi[0]][tas_asagi[1]] == rakip1:
            if tahta[tas_asagi[0] + 1][tas_asagi[1]] == oyuncu1:
                tahta[tas_asagi[0]][tas_asagi[1]] = " "
    except IndexError:
        pass

    # Taşın yukarısındaki taşların kontrol edilip rakip taşın kilitlenip kilitlenmediğini kontrol edilmesi

    try:
        tas_yukari = [tas[0] - 1, tas[1]]
        if tahta[tas_yukari[0]][tas_yukari[1]] == rakip1:
            if tahta[tas_yukari[0] - 1][tas_yukari[1]] == oyuncu1:
                tahta[tas_yukari[0]][tas_yukari[1]] = " "
    except IndexError:
        pass

    # Köşedeki taşların kilitlenmesi

    # Sol üst köşedeki taşın kilitlenip kilitlenmediğinin kontrol edilmesi

    try:
        if tas in [[0, 1], [1, 0]]:
            if tahta[0][1] == oyuncu1 and tahta[1][0] == oyuncu1 and tahta[0][0] == rakip1:
                tahta[0][0] = " "
    except IndexError:
        pass

    # Sol alt köşedeki taşın kilitlenip kilitlenmediğinin kontrol edilmesi

    try:
        if tas in [[sayi - 1, 1], [sayi - 2, 0]]:
            if tahta[sayi - 1][1] == oyuncu1 and tahta[sayi - 2][0] == oyuncu1 and tahta[sayi - 1][0] == rakip1:
                tahta[sayi - 1][0] = " "
    except IndexError:
        pass

    # Sağ üst köşedeki taşın kilitlenip kilitlenmediğinin kontrol edilmesiH

    try:
        if tas in [[0, sayi - 2], [1, sayi - 1]]:
            if tahta[0][sayi - 2] == oyuncu1 and tahta[1][sayi - 1] == oyuncu1 and tahta[sayi - 1][0] == rakip1:
                tahta[0][sayi - 1] = " "
    except IndexError:
        pass

    # Sağ alt köşedeki taşın kilitlenip kilitlenmediğinin kontrol edilmesi

    try:
        if tas in [[sayi - 1, sayi - 2], [sayi - 2, sayi - 1]]:
            if tahta[sayi - 1][sayi - 2] == oyuncu1 and tahta[sayi - 2][sayi - 1] == oyuncu1 and tahta[sayi - 1][
                sayi - 1] == rakip1:
                tahta[sayi - 1][sayi - 1] = " "
    except IndexError:
        pass


# Oyun tahtasını yazdırmaya yarayan fonksiyon

def yazdir(harf, sayi, tahta):
    print("    ", end="")
    for k in harf:
        print(f"  {k}   ", end="")
    print()
    for i in range(sayi):
        tmp2 = sayi - 1
        print("   |" + "------" * tmp2 + "-----|")
        print(f"{i + 1}  |", end="")
        for j in range(sayi):
            print(f"  {tahta[i][j]:.3}  ", end="|")
        print(f" {i + 1}")
    print("    " + "------" * sayi)
    print("    ", end="")
    for k in harf:
        print(f"  {k}   ", end="")
    print()


# Oyun için gerekli olan fonksiyonların ana fonksiyonda çağırılması

def main():
    sayi = sayi_al()
    sira = 0
    oyuncu = input("İlk oyuncunun sembolü: ")
    rakip = input("İkinci oyuncunun sembolü: ")
    tahta = liste_olustur(int(sayi), oyuncu, rakip)
    harf = ["A", "B", "C", "D", "E", "F", "G", "H"]
    harf = harf[:sayi]
    yazdir(harf, sayi, tahta)
    while True:
        oyuncu_tas = 0
        rakip_tas = 0
        for i in tahta:
            oyuncu_tas += i.count(oyuncu)
            rakip_tas += i.count(rakip)
        if oyuncu_tas < 2:
            print(f"{rakip} kazandı")
            break
        elif rakip_tas < 2:
            print(f"{oyuncu} kazandı")
            break
        tas = hareket(sira, sayi, tahta, rakip, oyuncu, harf)
        kilit(tas, rakip, oyuncu, tahta, sayi, sira)
        sira += 1
        yazdir(harf, sayi, tahta)


# Tüm fonksiyonları çalıştıracak olan ana fonksiyonun çağırılması

main()