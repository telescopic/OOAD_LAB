from tkinter import *

undo_list=[]
undo_list_num=[]
undo_list_den=[]
cntr_row=5
root = Tk()
root.geometry("1500x700")
root.title("Student companion system")

w=Canvas(root,width=1200,height=700)
w.configure(bg="black")
w.create_line(100,0, 100,1200, fill="red")

Label(root,text="\n          ATTENDANCE MANAGER MODULE\n",font=("Calibri",20)).grid(row=0,column=1)
Label(root,text=" Enter subject name to add : ",font=("Calibri",16)).grid(row=1,column=1)
Label(root,text="   ").grid(row=2,column=1)
Label(root,text="Subjects",font=("Calibri",20)).grid(row=3,column=1)
T=Text(root,font=("Calibri",15),width=20,height=2)
T.grid(row=1,column=2)
class Obj:
  def __init__(self,rt,txt,r):
    self.cur=0
    self.tot=0
    self.rt=rt
    self.L=Label(self.rt,text=txt,font=("Calibri",16))
    self.L.grid(row=r,column=1,pady=(10,10))
    self.B=Button(self.rt,text="Mark Present",font=("Calibri",16),command=self.present)
    self.B.grid(row=r,column=2,pady=(10,10))
    self.BB=Button(self.rt,text="Mark Absent",font=("Calibri",16),command=self.absent)
    self.BB.grid(row=r,column=3,pady=(10,10))
    self.rem=Button(self.rt,text="Remove",font=("Calibri",16),command=self.remv)
    self.rem.grid(row=r,column=4,padx=(10,10),pady=(10,10))
    self.v=StringVar()
    self.L1=Label(self.rt,textvariable=self.v,font=("Calibri",20))
    self.L1.grid(row=r,column=5,pady=(10,10),padx=(20,20))
  def present(self):
    self.cur+=1
    self.tot+=1
    temp=str(int(100*self.cur/self.tot))
    self.v.set("Total attendance: "+str(self.cur)+"/"+str(str(self.tot))+" Attendance %: "+temp)
  def absent(self):
    self.tot+=1
    temp=str(int(100*self.cur/self.tot))
    self.v.set("Total attendance: "+str(self.cur)+"/"+str(str(self.tot))+" Attendance %: "+temp)
  def remv(self):
    self.L.grid_remove()
    self.B.grid_remove()
    self.BB.grid_remove()
    self.rem.grid_remove()
    self.L1.grid_remove()
def add_subject():
    if(T.get("1.0",'end-1c')==""):
        return
    p=Obj(root,T.get("1.0",'end-1c'),cntr_row)
    inc()
def inc():
    global cntr_row
    cntr_row+=2
Button(root,text="Add subject",width=10,height=2,command=add_subject).grid(row=1,column=3)
root.mainloop()


