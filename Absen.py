from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

print('''pelajaran apa bro
1. Agama
2. pkn
3. indo
4. mtk
5. ipa
6. ips
7. inggris
8. sbd
9. pjok
10. tik
11. sunda''')
x = int(input("Input: "))

# Nama & Kelas
kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[9]'
# Pelajaran
agama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]'
pkn = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[4]'
indo = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[5]'
mtk = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[6]'
ipa = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[7]'
ips = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[8]'
eng = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[9]'
sbd = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[10]'
pjok = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[11]'
tik = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[12]'
sunda = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[13]'

# Mulai web
print("Memulai Web Browser")
web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')

# Pilih Kelas
time.sleep(2)
kelas = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]')
kelas.click()
time.sleep(1)
kelas96 = web.find_element_by_xpath(kelas96)
kelas96.click()
time.sleep(1)
berikutnya = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span')
berikutnya.click()
print("Selesai memilih kelas")

# Pilih Nama
time.sleep(2)
pilihNama = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]')
pilihNama.click()
time.sleep(1)
nama = web.find_element_by_xpath(nama)
nama.click()
time.sleep(2)
berikutnya = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span')
berikutnya.click()
print("Selesai memilih nama")

# Pilih Pelajaran
time.sleep(2)
pilihPelajaran = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]')
pilihPelajaran.click()
time.sleep(1)

# Pelajaran
if x == 1:
    agama = web.find_element_by_xpath(agama)
    agama.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 2:
    pkn = web.find_element_by_xpath(pkn)
    pkn.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 3:
    indo = web.find_element_by_xpath(indo)
    indo.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 4:
    mtk = web.find_element_by_xpath(mtk)
    mtk.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 5:
    ipa = web.find_element_by_xpath(ipa)
    ipa.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 6:
    ips = web.find_element_by_xpath(ips)
    ips.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 7:
    eng = web.find_element_by_xpath(eng)
    eng.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 8:
    sbd = web.find_element_by_xpath(sbd)
    sbd.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 9:
    pjok = web.find_element_by_xpath(pjok)
    pjok.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 10:
    tik = web.find_element_by_xpath(tik)
    tik.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

elif x == 11:
    sunda = web.find_element_by_xpath(sunda)
    sunda.click()
    time.sleep(1)
    pilihHadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    pilihHadir.click()
    time.sleep(1)
    hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]')
    hadir.click()

print("Selesai memilih pelajaran")
