import sqlite3

def lic_data():
        con=sqlite3.connect("rto_dat.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS rto (lic INTEGER PRIMARY KEY,name text,accident text,dob text)")
        con.commit()
        con.close()

def addrec (lic,name,accident,dob):
        con=sqlite3.connect("rto_dat.db")
        cur=con.cursor()
        cur.execute ("INSERT OR IGNORE INTO rto VALUES (?,?,?,?)",(lic,name,accident,dob))
        con.commit()
        con.close()

def viewdata ():
        con=sqlite3.connect("rto_dat.db")
        cur=con.cursor()
        cur.execute ("SELECT * FROM rto")
        row=cur.fetchall()
        con.close()
        return row

def deleterec(lic):
        con=sqlite3.connect("rto_dat.db")
        cur=con.cursor()
        cur.execute("DELETE FROM rto WHERE lic=?",(lic,))
        con.commit()
        con.close

def searchdata(lic):
        con=sqlite3.connect("rto_dat.db")
        cur=con.cursor()
        cur.execute("SELECT * FROM rto WHERE lic=?",(lic,))
        row=cur.fetchall()
        con.close()
        return row


lic_data()
