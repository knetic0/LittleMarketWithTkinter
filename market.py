from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('1360x768')
root.resizable(True,True)
root.title('OKUMARKT')

def urunler():
	urun = []

	for i in liste.curselection():
		urun.append(liste.get(i))

	if urun[0] == 'Sebzeler':
		global toplam
		toplam = 0
		spinBox1 = Spinbox(root,from_=-0,to=5,font=('Calibri',12))
		spinBox1.grid(row=2,column=2,rowspan=5)

		fiyat1 = Label(root,text='6.00TL',font=('Calibri',14))
		fiyat1.grid(row=2,column=2,columnspan=2)

		list1 = Listbox(root,font=('Calibri'),height=1,width=11)
		list1.grid(row=2,column=2)


		spinBox2 = Spinbox(root,from_=-0,to=5,font=('Calibri',12))
		spinBox2.grid(row=2,column=3,rowspan=5)

		fiyat2 = Label(root,text='10.00TL',font=('Calibri',14))
		fiyat2.grid(row=2,column=3,columnspan=2)

		list2 = Listbox(root,font=('Calibri'),height=1,width=11)
		list2.grid(row=2,column=3,columnspan=1)


		spinBox3 = Spinbox(root,from_=-0,to=5,font=('Calibri',12))
		spinBox3.grid(row=2,column=4,rowspan=5)

		fiyat3 = Label(root,text='12.00TL',font=('Calibri',14))
		fiyat3.grid(row=2,column=4,columnspan=14)

		list3 = Listbox(root,font=('Calibri'),height=1,width=11)
		list3.grid(row=2,column=4,columnspan=1)

		def satinAlIslem():
			global toplam
			toplam=0
			toplam += int(spinBox1.get()) * 6 + int(spinBox2.get()) * 10 + int(spinBox3.get()) * 12
			
			alinanlar = Listbox(root,font=('Calibri',24))
			alinanlar.grid(row=2,column=4,columnspan=150)

			alinanlar.insert(0,spinBox1.get() + ' KG Domates')
			alinanlar.insert(1,spinBox2.get() + ' KG Patlican')
			alinanlar.insert(2,spinBox3.get() + ' KG Ispanak')
			alinanlar.insert(3,'Toplam fiyat = ' + str(toplam) + ' TL')


		alButton = Button(root,text='Satin Al',font=('Calibri',16),command=satinAlIslem)
		alButton.grid(row=3,column=2,rowspan=5)

		list1.insert(0,'---Domates---')
		list2.insert(0,'---Patlican---')
		list3.insert(0,'---Ispanak---')
		

welcomeLabel = Label(root,text="OKUMARKT'a HOSGELDINIZ!",
					font=('Calibri',36))
welcomeLabel.grid(padx=500,columnspan=50)
#URUN LISTE------------------------
liste = Listbox(root,font=('Calibri',24),width=18)
liste.grid(row=2,column=1)

liste.insert(0,'Sebzeler')
liste.insert(1,'Meyveler')
liste.insert(2,'Et ve Sut Urunleri')
liste.insert(3,'Temizlik Urunleri')
liste.insert(4,'Erkek Urunleri')
liste.insert(5,'Kadin Urunleri')
liste.insert(6,'Erkek Cocuk Urunleri')
liste.insert(7,'Kiz Cocuk Urunleri')
liste.insert(8,'Teknoloji')
liste.insert(9,'Oyun, Eglence')
liste.insert(10,'Kitap')
liste.insert(11,'Spor Urunleri')
liste.insert(12,'Otomotiv')
liste.insert(13,'Dekorasyon')
liste.insert(14,'Oyuncak')
liste.insert(15,'Mobilya')

liste.config(height=liste.size())
#URUN LISTE------------------------


submitButton = Button(root,text='Sec',font=('Calibri',24),command=urunler)
submitButton.grid(row=3,column=1)


root.mainloop()