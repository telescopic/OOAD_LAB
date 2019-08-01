from tkinter import *

d_obj=[]
cntr_row=5
root = Tk()
root.geometry("1500x1000")
root.title("Student companion system")


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
    self.L.grid(row=r,column=1,pady=(5,5))
    self.B=Button(self.rt,text="Mark Present",font=("Calibri",16),command=self.present)
    self.B.grid(row=r,column=2,pady=(5,5))
    self.BB=Button(self.rt,text="Mark Absent",font=("Calibri",16),command=self.absent)
    self.BB.grid(row=r,column=3,pady=(5,5))
    self.rem=Button(self.rt,text="Remove",font=("Calibri",16),command=self.remv)
    self.rem.grid(row=r,column=4,padx=(10,10),pady=(5,5))
    self.v=StringVar()
    self.L1=Label(self.rt,textvariable=self.v,font=("Calibri",20))
    self.L1.grid(row=r,column=5,pady=(10,10),padx=(20,20))
    self.lnum=0
    self.lden=0
  def present(self):
    global d_obj
    d_obj.append(self)
    self.lnum=self.cur
    self.lden=self.tot
    self.cur+=1
    self.tot+=1
    temp=str(int(100*self.cur/self.tot))
    self.v.set("Total attendance: "+str(self.cur)+"/"+str(str(self.tot))+" Attendance %: "+temp)
  def absent(self):
    global d_obj
    d_obj.append(self)
    self.lnum=self.cur
    self.lden=self.tot
    self.tot+=1
    temp=str(int(100*self.cur/self.tot))
    self.v.set("Total attendance: "+str(self.cur)+"/"+str(str(self.tot))+" Attendance %: "+temp)
  def remv(self):
    for i in range(0,len(d_obj)):
        if d_obj[i] is self:
            del d_obj[i]
    self.L.grid_remove()
    self.B.grid_remove()
    self.BB.grid_remove()
    self.rem.grid_remove()
    self.L1.grid_remove()
  def last(self):
    self.cur=self.lnum
    self.tot=self.lden
    temp=str(int(100*self.cur/max(self.tot,1)))
    self.v.set("Total attendance: "+str(self.cur)+"/"+str(str(self.tot))+" Attendance %: "+temp)

def add_subject():
    if(T.get("1.0",'end-1c')==""):
        return
    p=Obj(root,T.get("1.0",'end-1c'),cntr_row)
    inc()
def inc():
    global cntr_row
    cntr_row+=2
def ud():
    if(len(d_obj)==0):
        return
    d_obj[len(d_obj)-1].last()
    d_obj.pop()
Button(root,text="Add subject",width=10,height=2,command=add_subject).grid(row=1,column=4)
##Label(root,text="           ").grid(row=1,column=5)
BBB=Button(root,text="Undo",width=10,height=2,command=ud)
BBB.grid(row=1,column=5)
root.mainloop()


