from tkinter import *

def view(filename):
    f = open(filename, encoding='utf-8')
    text1.delete(1.0, END)
    text1.insert(1.0, f.read())
    f.close()

def change():
    files = ['Київ.txt', 'Львів.txt', 'Дніпро.txt', 'Одеса.txt', 'Харків.txt', 'Ужгород.txt', 'Івано-Франківськ.txt']
    view(files[var.get()])

def create_files():
    city_info = {
        'Київ.txt': 'Київ — столиця України, одне з найбільших і найстаріших міст Європи. Розташований на річці Дніпро, є центром Київської агломерації. Окрема адміністративно-територіальна одиниця України й адміністративний центр Київської області. Адміністративно до складу Київської області не входить.',
        'Львів.txt': 'Львів — місто обласного значення в Україні, адміністративний центр Львівської області, національно-культурний та освітньо-науковий осередок країни, великий промисловий центр і транспортний вузол. За кількістю населення — сьоме місто країни.',
        'Дніпро.txt': 'Дніпро — місто, адміністративний центр Дніпропетровської області України, центр Дніпровської агломерації. Четверте за чисельністю населення місто країни після Києва, Харкова та Одеси.',
        'Одеса.txt': 'Одеса — місто на чорноморському узбережжі України, найбільший морський порт в країні, місто обласного значення, центр Одеської агломерації. Адміністративний центр Одеської області і Одеського району.',
        'Харків.txt': 'Харків — місто на північному сході України. Розташоване на межі водорозділу басейнів річок Дніпра і Дону. Друге за чисельністю населення місто України після Києва.',
        'Ужгород.txt': 'Ужгород — адміністративний центр Закарпатської області та Ужгородського району, місто обласного значення. Розташований на річці Уж. Політичний, економічний, науковий і культурний центр Закарпатської області.',
        'Івано-Франківськ.txt': 'Івано-Франківськ — місто обласного значення в Україні, адміністративний центр Івано-Франківської області та Івано-Франківського району. Розташоване на південному заході України, на стику гір та рівнин в передгір\'ї Українських Карпат.'
    }
    
    for filename, content in city_info.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

create_files()

root = Tk()
root.title('Міста України')

text1 = Text(width=40, height=10, wrap=WORD)
text1.grid(row=0, column=1, rowspan=10, padx=10, pady=10)

var = IntVar()
var.set(0)

kyiv = Radiobutton(text='Київ', variable=var, value=0, command=change)
lviv = Radiobutton(text='Львів', variable=var, value=1, command=change)
dnipro = Radiobutton(text='Дніпро', variable=var, value=2, command=change)
odesa = Radiobutton(text='Одеса', variable=var, value=3, command=change)
kharkiv = Radiobutton(text='Харків', variable=var, value=4, command=change)
uzhgorod = Radiobutton(text='Ужгород', variable=var, value=5, command=change)
frankivsk = Radiobutton(text='Івано-Франківськ', variable=var, value=6, command=change)

kyiv.grid(row=0, column=0, sticky=W)
lviv.grid(row=1, column=0, sticky=W)
dnipro.grid(row=2, column=0, sticky=W)
odesa.grid(row=3, column=0, sticky=W)
kharkiv.grid(row=4, column=0, sticky=W)
uzhgorod.grid(row=5, column=0, sticky=W)
frankivsk.grid(row=6, column=0, sticky=W)

change()

root.mainloop()