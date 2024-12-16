import tkinter
from symtable import Class

window=tkinter.Tk()
window.title("Vucut kitle endeksi")
window.config(pady=30,padx=30)

def vke_hesaplama():
    Boy=HeightInput.get()
    Kilo=WeightInput.get()
    if Kilo == "" or Boy == "":
        ReulstLabel.config(text="Kilo ve boyunuzu giriniz!")
    else:
        try:
            vke=float(Kilo)/((float(Boy)/100)**2)
            result_string=vke_sonuc(vke)
            ReulstLabel.config(text=result_string)
        except:
            ReulstLabel.config(text="Lutfen sayi giriniz!")


#arayuz
WeightInputLabel=tkinter.Label(text="Lutfen kilonuzu giriniz (kg): ")
WeightInputLabel.pack()

WeightInput=tkinter.Entry(width=10)
WeightInput.pack()

HeightInputLabel=tkinter.Label(text="Lutfen boyunuzu giriniz (cm): ")
HeightInputLabel.pack()

HeightInput=tkinter.Entry(width=10)
HeightInput.pack()

CalculateButton=tkinter.Button(text="Hesapla",command=vke_hesaplama)
CalculateButton.pack()

ReulstLabel=tkinter.Label()
ReulstLabel.pack()

def vke_sonuc(vke):
    result_string = f"Vucut kitle endeksiniz {round(vke, 2)}. "
    if vke <= 16:
        result_string += "zayifsiniz!"
    elif 16 < vke <= 17:
        result_string += "oldukca ince!"
    elif 17 < vke <= 18.5:
        result_string += "hafif ince!"
    elif 18.5 < vke <= 25:
        result_string += "kilonuz normal"
    elif 25 < vke <= 30:
        result_string += "kilolusunuz"
    elif 30 < vke <= 35:
        result_string += "obez 1.sinif"
    elif 35 < vke <= 40:
        result_string += "obez 2.sinif"
    else:
        result_string += "obez 3.sinif"
    return result_string


window.mainloop()