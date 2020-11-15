from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from termcolor import colored
import bcolors


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

# //////////////////////// XPATH ////////////////////////
kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[9]'
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
kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]' 
berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'

#//////////////////////// Mulai web ////////////////////////
print("Memulai Web Browser")
web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
time.sleep(0.7)

now = datetime.now().time()
    
#//////////////////////// Pilih Kelas////////////////////////
kelas = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, kelas))
)
kelas.click()

kelas96 = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, kelas96))
)
kelas96.click()
time.sleep(0.7)

nextbutton2 = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, nextbutton1))
)
web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
nextbutton2.click()

print('[', now, ']', 'KELAS SELECTED')

#////////////////////////CHOOSING NAME////////////////////////
pilihNama = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihNama))
)
pilihNama.click()

nama = WebDriverWait(web, 10).until(
    EC.visibility_of_element_located((By.XPATH, nama))
)
nama.click()
time.sleep(0.7)

berikutnya = WebDriverWait(web, 10).until(
    EC.visibility_of_element_located((By.XPATH, berikutnya))
)
berikutnya.click()

now2 = datetime.now().time()
print('[', now2, ']', 'NAME SELECTED')

# ////////////////////////Pilih Pelajaran////////////////////////
pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
)
pilihPelajaran.click()

# ////////////////////////- if Pelajaran////////////////////////
if x == 1:
    agama = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, agama))
    )
    agama.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )

elif x == 2:
    pkn = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pkn))
    )
    pkn.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 3:
    indo = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, indo))
    )
    indo.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 4:
    mtk = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, mtk))
    )
    mtk.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 5:
    ipa = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, ipa))
    )
    ipa.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 6:
    ips = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, ips))
    )
    ips.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 7:
    eng = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, eng))
    )
    eng.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 8:
    sbd = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, sbd))
    )
    sbd.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 9:
    pjok = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pjok))
    )
    pjok.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 10:
    tik = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, tik))
    )
    tik.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()

elif x == 11:
    sunda = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, sunda))
    )
    sunda.click()
    time.sleep(0.7)
    pilihHadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, pilihHadir))
    )
    pilihHadir.click()
    hadir = WebDriverWait(web, 10).until(
        EC.element_to_be_clickable((By.XPATH, hadir))
    )
    hadir.click()    


#////////////////////////submit////////////////////////
submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
)
#submit.click()
now3 = datetime.now().time()
print('[', now3, ']', 'SUBMITTED')

