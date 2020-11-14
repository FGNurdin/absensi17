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
x = int(input())

web = webdriver.Chrome()
web.get('https://docs.google.com/forms/d/e/1FAIpQLSfhQ1Nxrrzbo1kv_yZW5KoCTTpSqd5htdQIhT5tAIFFqM_few/viewform?usp=sf_link')


nextButton = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div/span')
time.sleep(2)
kelas = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div[1]')
kelas.click()


time.sleep(2)
kelas96 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div[8]')
kelas96.click()
nextButton.click()
print('kelas udah bos')

nextButton = web.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
nama = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]')
nama.click()

time.sleep(2)
fatih = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[15]')
fatih.click()
web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
nextButton2 = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div/div[2]/span')
nextButton2.click()
print('nama juga udah bos')
time.sleep(2)

pelajaran = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]')
pelajaran.click()
time.sleep(2)







print('bp1')




hadir = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
print('bp2')
if x == 1:
    print(x)
    agama = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]')
    agama.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 2:
    print(x)
    pkn = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[4]')
    pkn.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 3:  
    print(x)
    indo = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[5]')
    indo.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 4:
    mtk = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[6]')
    mtk.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 5:
    ipa = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[7]')
    ipa.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 6:
    ips = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[8]')
    ips.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 7:
    inggris = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[9]')
    inggris.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 8:
    sbd = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[10]')
    sbd.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 9:
    pjok = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[11]')
    pjok.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 10:
    tik = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[12]')
    tik.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()

if x == 11:
    sunda = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[13]')
    sunda.click()
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    hadir.click()
    hadirOpt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
    hadirOpt.click()    


    