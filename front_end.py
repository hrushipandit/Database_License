
from tkinter import *
import tkinter.messagebox
import back_end

class RTO:

    def __init__(self,root):
        self.root=root
        self.root.title="RTO license records"
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="lavender")

        lic=StringVar()
        name=StringVar()
        dob=StringVar()
        accident=StringVar()
        temp_lic=StringVar()

       # BottomFrame=Frame(self.root)

#=======================Frames===================================


        MainFrame=Frame(self.root,bg="WHITE")
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,bd=2,padx=450,pady=20,bg="Cadet Blue",relief=RIDGE)
        TitleFrame.grid(row=0,column=0,columnspan=2)

        self.lb1Tit=Label(TitleFrame,font=('arial',47,'bold'),text="RTO License Records",bg="White")
        self.lb1Tit.grid()

        Frame_input = LabelFrame (MainFrame,bd=2,width=850,height=400,padx=0,pady=20,bg="Ghost White",font=('arial',30,'bold'),text='Input Info\n')
        Frame_input.grid(row=1,column=0)

        Frame_output = LabelFrame (MainFrame, bd=2, width= 700,height=400,padx=10,pady=0,bg="Ghost White",font=('arial',30,'bold'),text='Output Info\n')
        Frame_output.grid(row=1,column=1)

        Frame_query = LabelFrame (MainFrame, width=1600, height=250,padx=0,pady=0,bg="gray25",text='Search by',font=('arial',30,'bold'))
        Frame_query.grid(row=2,column=0,columnspan=2)

        
#=================================Labels====================

        lic_label = Label (MainFrame,font=('arial',20,'bold'),text='License Number:')
        lic_label.place (x=50,y=180)
        lic_entry = Entry (MainFrame,font=('arial',20,'bold'),textvariable= lic)
        lic_entry.place (x=370,y=180)
        

        name_label = Label (MainFrame,font=('arial',20,'bold'),text='Name:')
        name_label.place (x=50,y=220)
        name_entry = Entry (MainFrame,font=('arial',20,'bold'),textvariable=name)
        name_entry.place (x=370,y=220)

        acc_label = Label (MainFrame,font=('arial',20,'bold'),text='Accidents involved in:')
        acc_label.place (x=50,y=260)
        acc_entry = Entry (MainFrame,font=('arial',20,'bold'),textvariable=accident)
        acc_entry.place (x=370,y=260)
        

        DOB_label = Label (MainFrame,font=('arial',20,'bold'),text='DOB:')
        DOB_label.place (x=50,y=300)
        DOB_entry = Entry (MainFrame,font=('arial',20,'bold'),textvariable=dob)
        DOB_entry.place (x=370,y=300)

        scrollbar= Scrollbar(MainFrame)
        scrollbar.place(x=950,y=180)

        

        output_lb= Listbox (MainFrame,width=32,height=10,font=('arial',20,'bold'))
        output_lb.place(x=1000,y=180)
        scrollbar.config(command=output_lb.yview)


#========================Functions=======================
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("RTO","Confirm if you want to exit?")
            if iExit>0:
                root.destroy()
                return

        def add_data ():
            if (len(lic.get())!=0):
                back_end.addrec(lic.get(),name.get(),accident.get(),dob.get())
                output_lb.delete(0,END)
                output_lb.insert(END,(lic.get(),name.get(),accident.get(),dob.get()))

        def display():
            output_lb.delete(0,END)
            for row in back_end.viewdata():
                output_lb.insert(END,row,str(""))

        def delete():
            back_end.deleterec(temp_lic.get())
            display()

        def search():
            output_lb.delete(0,END)
            for row in back_end.searchdata(temp_lic.get()):
                output_lb.insert(END,row,str(""))

#=============================Buttons=======================


        lic_search = Button (MainFrame,font=('arial',20,'bold'),text='License No',height=1,width=10,bd=4,command=search)
        lic_search.place (x=50,y=600)
    
        acc_search = Button (MainFrame,font=('arial',20,'bold'),text='Delete',height=1,width=10,bd=4,command=delete)
        acc_search.place (x=350,y=600)

        name_search = Button (MainFrame,font=('arial',20,'bold'),text='Show all',height=1,width=10,command=display)
        name_search.place (x=650,y=600)
    
        input_search = Entry (MainFrame,font=('arial',20,'bold'),textvariable=temp_lic)
        input_search.place (x=950,y=600)

        take_input = Button (MainFrame, font=('arial',20,'bold'),text='Add Data',height=1,width=10,bd=4,command=add_data)
        take_input.place (x=370,y=360)

        exit_button = Button (MainFrame,font=('arial',20,'bold'),text='Exit',height=1,width=10,command=iExit)
        exit_button.place (x=1300,y=50)


                
if __name__=="__main__":
    root=Tk()
    application = RTO(root)
    root.mainloop()
