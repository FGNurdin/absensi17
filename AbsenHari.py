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

print('''hari apa bro
1. Senin
2. Selasa
3. Rabu
4. Kamis
5. Jumat''')
x = int(input("Input: "))

#//////////////////////// Mulai web ////////////////////////
def agama1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    agama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def pkn1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    pkn = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[4]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()

    
def indo1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    indo = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[5]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def mtk1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    mtk = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[6]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def ipa1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    ipa = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[7]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def ips1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    ips = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[8]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def eng1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    eng = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[9]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def sbd1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    sbd = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[10]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def pjok1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    pjok = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[11]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def tik1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    tik = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[12]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()


def sunda1():
    #//////////////////////// Xpath ////////////////////////
    pilihNama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]'
    kelas96 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[8]'
    berikutnya = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div[2]/span'
    nama = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]'
    nextbutton1 = '//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div/div/div/span/span'
    sunda = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[13]'
    pilihPelajaran = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    pilihHadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]'
    hadir = '//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]'
    submit = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span'
    #//////////////////////// Start ////////////////////////
    print("Memulai Web Browser")
    web = webdriver.Chrome()
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSfm01iI_3HfT1DXHdgFa30bY0ooVcSp0SRHemh_klIIXo8-Jw/viewform?embedded=true')
    time.sleep(0.7)
    
    now = datetime.now().time()
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
    #//////////////////////// Nama ////////////////////////
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
    #//////////////////////// Pelajaran ////////////////////////
    pilihPelajaran = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, pilihPelajaran))
    )
    pilihPelajaran.click()
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
    # ////////////////////// Submit ////////////////////////
    submit = WebDriverWait(web, 10).until(
    EC.element_to_be_clickable((By.XPATH, submit))
    )
    #submit.click()
    now3 = datetime.now().time()
    print('[', now3, ']', 'SUBMITTED')
    web.close()

if x == 1:
    mtk1()
    time.sleep(10)
    pkn1()
    time.sleep(10)
    ipa1()

elif x == 2:
    indo1()
    time.sleep(7)
    sunda1()
    time.sleep(7)
    sbd1()

elif x == 3:
    ipa1()
    time.sleep(7)
    pjok1()
    time.sleep(7)
    indo1()

elif x == 4:
    eng1()
    time.sleep(7)
    tik1()
    time.sleep(7)
    mtk1()

elif x ==5:
    agama1()
    time.sleep(7)
    ips1()

else:
    exit()