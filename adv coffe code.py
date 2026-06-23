from tkinter import*
from datetime import datetime
import random
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
    result.config(text="..........................\n"
                  "SHREYANSH COFFEE CAFE\n"
                  ".....................\n\n"
                  "Bill NO" + str(bill_no)+
                  "\nDate and Time:"+str(current_time)+
                  "\nCUSTOMER:  "+customer_name +
                  "\ntotal bill Rs: "+ str(total)+
                  "\nGST (26%): "+ str(gst)+
                  "\n discount RS " + str(discount)+
                  "\nGrand Total: "+str(grand_total)+
                  "\n\n\n.........................."+
                  "\nTHANK YOU"+
                  "\n================================")
root=Tk()
root.title(" SHREYANSH COFFE CAFE")
root.geometry("400x550")
Label(root,text=" Shreyansh coffee cafe menu",font=("Arial",14)).pack()
Label(root,text=" Enter Customer Name",font=("Arial",14)).pack()
name=Entry(root)
name.pack()
expresso_var=IntVar()
Cafechino_var=IntVar()
Latte_var=IntVar()
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
Button(root,text=("Genrate Bill"),command=bill).pack(pady=10)
result=Label(root,text=" ")
result.pack()
root.mainloop()
