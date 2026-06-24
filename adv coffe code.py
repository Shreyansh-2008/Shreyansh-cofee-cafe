from tkinter import*
from datetime import datetime
import random
from tkinter import messagebox
def bill():
    customer_name=name.get()
    total=0
    if expresso_var.get()==1:
       total+=100*int(expresso_qty.get())
    if Cafechino_var.get()==1:
      total+=150*int(Cafechino_qty.get())
    if Latte_var.get()==1:
      total+=200*int(Latte_qty.get())
    gst=total*0.26
    discount=0
    if total>= 1000:
        discount=total*0.10
    grand_total=total+gst-discount
    bill_no=random.randint(1000,9999)
    current_date=datetime.now().strftime("%d/%m/%y")
    current_time=datetime.now().strftime("%I:%M:%S%p")
    temp=temp_var.get()
    mood=mood_var.get()
    weather=weather_var.get()
    taste=taste_var.get()
    sugar=sugar_var.get()
    suggestion="NO RECOMMENDATION"
    if temp=="HOTt" and mood == "sleepy":
        suggestion="EXPRESSO RECOMMENED"
    elif temp=="warm" and taste == "sweet":
        suggestion="CAFECHINO RECOMMENED"
    elif temp=="cold" and sugar == "no sugar":
        suggestion="LATTE RECOMMEND"
    
    messagebox.showinfo(
"AI Coffee Advisor",
"Recommended Coffee: " + suggestion +
"\nBill No:" + str(bill_no))
root=Tk()

root=Tk()
root.title(" SHREYANSH COFFE CAFE")
root.geometry("1000x2000")
Label(root,text=" Shreyansh coffee cafe menu",font=("Arial",14)).pack()
Label(root,text=" Enter Customer Name",font=("Arial",14)).pack()
name=Entry(root)
name.pack()
expresso_var=IntVar()
Cafechino_var=IntVar()
Latte_var=IntVar()
weather_var=StringVar()
weather_var.set("NORMAL")
mood_var=StringVar()
mood_var.set("NORMAL")
temp_var=StringVar()
temp_var.set("NORMAL")
sugar_var=StringVar()
sugar_var.set("MEDIUM")
taste_var=StringVar()
taste_var.set("BALANCED")
Checkbutton(root,text="Express-100",variable=expresso_var).pack()
expresso_qty=Entry(root)
expresso_qty.insert(0,"1")
expresso_qty.pack()
Checkbutton(root,text="Cafechino-150",variable=Cafechino_var).pack()
Cafechino_qty=Entry(root)
Cafechino_qty.insert(0,"1")
Cafechino_qty.pack()
Checkbutton(root,text="Latte-200",variable=Latte_var).pack()
Latte_qty=Entry(root)
Latte_qty.insert(0,"1")
Latte_qty.pack()
Label(root,text="Weather").pack()
Radiobutton(root,text="Cold",
variable=weather_var,value="cold").pack()
Radiobutton(root,text="normal",
variable=weather_var,value="normal").pack()
Radiobutton(root,text="hot",
      variable=weather_var,value="hot").pack()
Label(root,text="mood").pack()
Radiobutton(root,text="Sleepy",
              variable=mood_var,value="sleepy").pack()
Radiobutton(root,text="normal",
variable=mood_var,value="normal").pack()
Radiobutton(root,text="energetic",
variable=mood_var,value="energetic").pack()
Label(root,text="coffee Temperature").pack()
Radiobutton(root,text="HOTT",
variable=temp_var,value="HOTT").pack()
Radiobutton(root,text="WARM",
variable=temp_var,value="WARM").pack()
Radiobutton(root,text="COLD",
variable=temp_var,value="COLD").pack()
Label(root,text="Taste Preference").pack()
Radiobutton(root,text="SWEET",
variable=taste_var,value="SWEET").pack()
Radiobutton(root,text="BALANCED",
variable=taste_var,value="BALANCED").pack()
Radiobutton(root,text="STRONG",
variable=taste_var,value="STRONG").pack()
Label(root,text="Sugar Preference").pack()
Radiobutton(root,text="no sugar",
variable=sugar_var,value="no sugar").pack()
Radiobutton(root,text="Less sugar",
variable=sugar_var,value="Less sugar").pack()
Radiobutton(root,text="Medium Sweet",
variable=sugar_var,value="Medium Sweet").pack()
Radiobutton(root,text="Extra sweet",
variable=sugar_var,value="Extra sweet").pack()
Button(root,text=("Genrate Bill"),command=bill).pack(pady=10)
result=Label(root,text=" ",justify=LEFT,anchor="w",font=("Courier",10),wraplength=350)
result.pack(pady=10)
root.mainloop()
