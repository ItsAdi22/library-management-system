from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from config import *

try:
    cur.execute("CREATE TABLE IF NOT EXISTS issuetable (id INTEGER, name VARCHAR(255));")
except Exception as e:
    print(f'Error Occurred: {e}')

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    bid = inf1.get()
    bid = int(bid)
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    cur.execute("SELECT bid FROM booktable")
    allbookid = cur.fetchall()

    allBid = []
    for x in allbookid:
        allBid.append(x[0])
        
    print(f"allbid ------> {allBid}")

  
    try:
        print(f'current bookid ---> {bid}')
        if bid in allBid:
            sql = ("SELECT status FROM booktable where bid = %s")
            values = (bid,)
            cur.execute(sql,values)
            checkstatus = cur.fetchone()
            print(f"check status ----> {checkstatus[0]} ---->type: {type(checkstatus)}")
                
            if str(checkstatus[0]) == 'avail': 
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    


    try:
        print(f'status value -----> {status}')
        if bid in allBid and status == True:

            insert_sql = "INSERT INTO issuetable VALUES (%s, %s)"
            values = (bid,issueto)
            cur.execute(insert_sql, values)
            con.commit()
        
            update_sql = "UPDATE booktable SET status = 'issued' WHERE bid = %s"
            value = (bid,)
            cur.execute(update_sql,bid)
            con.commit()
            
            
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            print(f"allbid clear ------> {allBid}")
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except Exception as e:
        print(f'ERROR OCCURRED: {e}')
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    allBid.clear()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()