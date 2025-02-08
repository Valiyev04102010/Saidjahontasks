# while True:
#     yosh = int(input("yoshingizni kiriting:"))
#     if yosh < 18 and  yosh > 1 :
#         print("siz hali yosh ekansiz")
#     elif yosh >=18 and yosh <=27 :
#         print("tabriklaymiz siz qabul qilindingiz")
#     elif yosh < 0:
#         print("lox deb oylayabsanmi")
#     else:
#         print("Afsuski qarib qobsiz")
#lesson_5
# list
# lst = [] lst=ozgaruvchi qavs listni funksiyasi list oziga xar xil malumotlarni bittada qabul qiladi
# lst = ["Saidjahon", 1,2,3,4,True,False]
#metodlar
# ismlar = ["Omadbek","Saidjahon","Gulsanam","Sunnatillo"]
# ismlar_2 = ["Omadbek","Saidjahon","Gulsanam","Sunnatillo"]
# print(ismlar)
# print(ismlar_2)
# # index-0dan boshlanadi
# print(ismlar[0])
# # listni metodlari
# print(ismlar.index("Gulsanam"))
# # index() - index aniqlab beradi
# # Qoshish metodlari
# ismlar.append("Dadada")
# print(ismlar)
# cars = ["BMW","PORSHE 911","LAMBARGINI HURAKAN","ROLLS-ROYCE CULINAN"]
# # pop =oziga bitta argument qabul qiladi -index qabul qiladi ochirish argumenti
# cars.pop(3)
# print(cars)
# while True:
#       son = int(input("olmalar sonini kirit:"))
#       son1 = int(input("oquvchilar sonini kirit:"))
#       if son > 0:
# #             print(f"{son%son1}ta olma qoldi")
# while True:
#       son = int(input("son kirit g'alcha:"))
#       if son > 0:
#             print(f"{son**3}shuni ozing topsang olasnmi")
#       else:
#             print("bizdan koproq foydalansang kelajakda tupoy bolasan")
# while True:
#       qizlar = int(input("sinfda nechtasizlar:"))
#       oquvchilar = 35
#       if qizlar <35:
#             print(f"demak ogil bolalar{oquvchilar - qizlar}ta")

# davlat_poytaxt = {
#         "Turkiya": "Anqara",
#         "O'zbekiston": "Toshkent",
#         "Rossiya": "Moskva",
#         "Fransiya": "Parij",
#         "Argentina": "Buyene Ayres",
#         "Yaponiya": "Tokyo",
#         "Qozog'iston": "Astana",
#  }
# for davlat, poytaxt in sorted(davlat_poytaxt_items()):
#  print(f'{davlat} ning poytaxti {poytaxt}.')
# davlat = input("davlatlarning nomini kiriting:")





# from bs4 import BeautifulSoup
# import requests
# url = "https://asaxiy.uz/product/kompyutery-i-orgtehnika/noutbuki/noutbuki-2"
# headers ={
#     'user-agent':
#     'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
# }
# request = requests.get(url,headers=headers)
# data = request.text
# data_base = []
# main = BeautifulSoup(data)
# block = main.find('div',class_='custom-gutter')
# product = block.find_all('div',class_='product__item')
# for item in product:
#     brand_name = item.find('span', class_='product__item__info-title').get_text()
#     brand_img = item.find('img', class_='img-fluid lazyload')
#     product_price = item.find('span', class_='product__item-price').get_text()
#     data_base.append({
#         'Brand_name':brand_name,
#         'Brand_img':brand_img,
#         'Product_price':product_price
#     })
#
# for x in data_base:
#         print(x)
# def qoshish():
#     son1 = int(input("son kirit:"))
#     son2 = int(input("son kirit:"))
#     natija = son1+son2
#     return f"{son1} va {son2}ning yigindisi {natija}ga teng"
# print(qoshish())

# def ayirish():
#     son1 = int(input("son kiriting"))
#     son2 = int(input("son kiriting"))
#     natija = son1-son2
#     return f"{son1} va {son2}ning ayirmasi {natija}ga teng"
# print(ayirish())
#
# def kopaytirish():
#     son1 = int(input("son kirit"))
#     son2 = int(input("son kirit"))
#     natija = son1*son2
#     if natija<= 0:
#         print("bu hato")
#     else:
#         print(f"{son1} bilan {son2}ning kopaytmasi {natija}ga teng")
#     return
# print(kopaytirish())

# def bolish():
#     son1 = int(input("son kirit"))
#     son2 = int(input("son kirit"))
#     natija = son1//son2
#     # if natija<=0:
#     #     print("eror")
#     return print(f"{son1} bilan {son2}ning bolinmasi {natija}ga teng")
# print(bolish())

# def olma():
#     son1 = int(input("olma nechta"))
#     son2 = int(input("omadga bervordim "))
#     natija = son1-son2
#     if natija<=0:
#         print("eror")
#     return print (f"{son1}  bilan {son2}ning ayirmasi {natija}ga teng")
# print (olma())

# def kub(a):
#     b = a**3
#     return f"darajasi({a})"

# lst = (100, 200, 300, 450)
# percent = int(input("foizni kiriting"))
# natija = [x*(percent/100) for x in lst]
# print(natija)

# while True:
#     soz = input("soz kirit:")
#     vowels = "aeiouAEIOU"
#     if soz[0] in vowels:
#         print("True")
#     else:
#         print("False")
# def kv():
#     a = int(input("son kirit:"))
#     b = int(input("son kirit:"))
#     return f"{a}ning {b} darajasi {a**b}ga teng"
# print(kv())
# def how_many_seconds(hours):
#     seconds = hours*60*60
#     return f"how_many_seconds({hours}) ➞ ({seconds})"
# print(how_many_seconds(hours = int(input("nechchi soat:"))))
# def remainder(a,b):
#     c = a % b
#     return f"remainder{a,b} ➞ {c}"
# print(remainder(a = int(input("son kirit:")),b = int(input("son kirit:"))))
# def yosh():
#     a = int(input("son kirit:"))
#     kunlar = a*365
#     return f"sen {a}yoshdasan va  bu {kunlar}kun boladi"
# print(yosh())
# def perimetr(a,b):
#     p = (a+b)*2
#     return f"{a}va {b}tomonli tog'ri tort burchakning P si {p}ga teng"
# print(perimetr(a = int(input("boyini kiriting:")),b = int(input("enini kiritong:"))))
# while True:
#     son = input("son kirit:")
#     vowels = "1", "2", "3", "4" ,"5", "6", "7", "8", "9"
#     if son[0!=2] in vowels:
#         print("polindrop")
#     else:
#         print("unpolindrop")
print("pppp")