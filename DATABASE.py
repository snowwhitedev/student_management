import sqlite3
conn = sqlite3.connect("company.db")
cur=conn.cursor()
#cur.execute("drop table if exists students")
cur.execute("CREATE TABLE if NOT exists students (\
    student_id INTEGER  PRIMARY KEY AUTOINCREMENT, \
    first_name VARCHAR (25) NOT NULL,\
    last_name VARCHAR (25) NOT NULL,\
    mark INT (3) DEFAULT 0,\
    active INT (3) DEFAULT 1,\
    image_location VARCHAR(25))")
conn.commit()
#conn.close
 
 
#cur.execute("insert into students (first_name, last_name)  values ('any','thing')")
#conn.commit()
 
cur.execute("select * from students")
rows = cur.fetchall()
print(rows)    
 
def View():
    conn = sqlite3.connect("company.db")
    cur = conn.cursor()
    cur.execute("select *  from students")
    rows = cur.fetchall()
    return rows
   
def Add(fname, lname, mark, active, imgloc):
    print(fname, lname, mark, active, imgloc)
    cur.execute("INSERT INTO students (first_name, last_name, mark, active, image_location) VALUES (?, ?, ?, ?, ?)",(fname, lname, mark, active, imgloc))
    conn.commit()

def Delete(id):
    print(id)
    sqlQeury = "DELETE FROM students WHERE student_id = ?"
    cur.execute(sqlQeury, (id,))
    conn.commit()

def Update(id, fname, lname, mark, active,imgloc):
    cur.execute("UPDATE students SET first_name = ?, last_name = ?, mark = ?, active=?, image_location=? WHERE student_id = ?", (fname, lname, mark, active, imgloc, id))
    conn.commit()

def Search(id, fname):
    if not id:
        print("OK")
        cur.execute("SELECT * FROM students WHERE first_name LIKE ?",  ('%' + fname +'%',))
    else:
        print(id)
        cur.execute("SELECT * FROM students WHERE student_id = ?", (id,))
    rows =cur.fetchall()
    return rows