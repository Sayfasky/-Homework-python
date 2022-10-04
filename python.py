from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import mysql.connector as mysql
class unit:
    def __init__(self,root):
        self.root=root
        self.root.title('Unit frame')
        self.root.geometry('720x700+300+50')
        unitid=StringVar()
        unitname=StringVar()
        def showdata():
            conn=mysql.connect(host='localhost',user='root',password='',database='dbbspa')
            cursor=conn.cursor()
            cursor.execute('select * from tbunit')
            result=cursor.fetchall()
            if(len(result)!=0):
                self.member_record.delete(*self.member_record.get_children())
                for row in result:
                    self.member_record.insert('',END,values=row)
                    cursor.execute('commit')
            conn.close()
            def SaveData():
                conn= mysql.connect(host='localhost',user='root',password='',database='db_bsp5')
                cursor=conn.cursor()
                cursor.execute('insert into tb_unit value(%s,%s)',(unitid.get(),unitname.get()))
                cursor.execute('commit')
                conn.close()
                ShowData()
            def EditData():
                conn= mysql.connect(host='localhost',user='root',password='',database='db_bsp5')
                cursor=conn.cursor()
                cursor.execute('insert into tb_unit value(%s,%s)',(unitid.get(),unitname.get()))
                cursor.execute('commit')
                conn.close()
                ShowData()





        #fonts=font('Time News Roman',16)
        # create mainframe5
        mainframe = Frame(self.root, bd=10, width=700, height=700, bg='cadetblue')
        mainframe.grid()
        # create titleframe
        titleframe = Frame(mainframe, bd=7, width=700, height=100, relief=RIDGE)
        titleframe.grid(row=0, column=0)
        # create middleframe
        middleframe = Frame(mainframe, bd=7, width=700, height=300, bg='cadetblue', relief=RIDGE)
        middleframe.grid(row=1, column=0)
        # create buttonframe
        buttonframe = Frame(mainframe, bd=7, width=700, height=100, bg='cadetblue', relief=RIDGE)
        buttonframe.grid(row=2, column=0)
        # create detailframe
        detailframe = Frame(mainframe, bd=7, width=700, height=100, bg='cadetblue', relief=RIDGE)
        detailframe.grid(row=3, column=0)
        # create letfframe
        letfframe = Frame(middleframe, bd=7, width=700, height=200, bg='cadetblue', relief=RIDGE)
        letfframe.pack(side=LEFT, padx=5, pady=0)
        # create innerframe
        innerframe = Frame(letfframe, bd=5, width=700, height=200, bg='azure')
        innerframe.pack(side=TOP, padx=5, pady=0)
        # --------------add wiget------------------
        fonts = ('Times New Roman', 14)
        lbltitle = Label(titleframe, font=('Times New Roman', 22), text='Unit manage', bg='cadetblue')
        lbltitle.grid(row=0, column=0)

        lblUnitID = Label(innerframe, font=fonts, text='Unit ID', width=10, justify=RIGHT)
        lblUnitID.grid(row=0, column=0)
        txtUnitID=Entry(innerframe,font=fonts,textvariable=unitid,width=15)
        txtUnitID.grid(row=0,column=1)

        lblUnitID = Label(innerframe, font=fonts, text='email', width=10, justify=RIGHT)
        lblUnitID.grid(row=1, column=0)
        txtUnitID = Entry(innerframe, font=fonts, textvariable=unitname, width=15)
        txtUnitID.grid(row=1, column=1)

        btnsave=Button(buttonframe,font=fonts,text='save', width=8,command=SaveData)
        btnsave.grid(row=0,column=0)
        btnedit = Button(buttonframe, font=fonts, text='edit', width=8, command='')
        btnedit.grid(row=0, column=1)
        btndelete = Button(buttonframe, font=fonts, text='delete', width=8, command='')
        btndelete.grid(row=0, column=2)
        btnexit = Button(buttonframe, font=fonts, text='exit', width=8, command='')
        btnexit.grid(row=0, column=3)

        #add scroll bar
        scroll_y=Scrollbar(detailframe,orient=VERTICAL)
        self.member_record=ttk.Treeview(detailframe,height=12,columns=('UnitID','UnitName' ),yscrollcommand=scroll_y)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.member_record.heading('UnitID',text='UnitID')
        self.member_record.heading('UnitName', text='UnitName')
        self.member_record.column('UnitID',width=200)
        self.member_record.column('UnitName',width=200)
        self.member_record.pack(fill=BOTH,expand=1)
        self.member_record.bind('buttonRelease-1','')





if(__name__=='__main__'):
    root=Tk()
    application=unit(root)
    root.mainloop()
