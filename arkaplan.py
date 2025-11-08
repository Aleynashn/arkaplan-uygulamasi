from tkinter import *
from tkinter import filedialog,messagebox
from rembg import remove
from PIL import Image,ImageTk
import io

#arkaplan kaldırma işlevi
 
def arkaplan_kaldir():
    try:
        # kullanıcıdan dosya seçmesini isteme
        girdi_dosya=filedialog.askopenfilename(
            title="Bir Görüntü Seçin",
            filetypes=[("Image files","*.jpg *.jpeg *.png")] #kabul edilen  dosya seçenekleri
        )
        #seçim yapılmazsa başa sar
        if not girdi_dosya:
            return
        cikti_dosya=filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files","*.png")],
            title="Çıktı Dosyasını Kayıt Et")
            
        if not cikti_dosya:
            return
        
        #görüntü oku ve arkaplanı kaldır

        with open(girdi_dosya,"rb") as dosya:
            girdi=dosya.read()
        sonuc=remove(girdi) #arkaplanı burda kaldırıyoruz

        #sonucu kaudet
        with open(cikti_dosya,"wb") as dosya:
            dosya.write(sonuc) #işlenmiş görüntüyü yeni dosyaya  yazar

            #çıktı görüntüsüne bir ön izleme ekle
        sonuc_goruntu=Image.open(io.BytesIO(sonuc)) #cıktıyı bellekte açar
        sonuc_goruntu.thumbnail((300,300))
        sonuc_img=ImageTk.PhotoImage(sonuc_goruntu)
        label_cikti.config(image=sonuc_img)
        label_cikti.image=sonuc_img

        messagebox.showinfo("Başarılı!","Arkaplan başarıyla kaldırıldı ve kaydedildi...")
    except Exception as e:
        messagebox.showerror("Hata!",f"Bir hata oluştu: {e}")

        #arayüzü kodla
pencere=Tk()
pencere.title("Arkaplan Kaldırma Uygulaması - Aleyna Şahin")
pencere.geometry("500x400")

#başlık etiketileri

label_baslik=Label(pencere, text="Fotoğraflardaki Arkaplanı Kaldır", font=("Arial",16))
label_baslik.pack(pady=10)

#buton ekle

buton_islem=Button(pencere,text="Görsel Seç ve Arkaplanı Kaldır",command=arkaplan_kaldir)
buton_islem.pack(pady=20)

#çıktı görüntüsü için label

label_cikti=Label(pencere)
label_cikti.pack(pady=10)

pencere.mainloop()













