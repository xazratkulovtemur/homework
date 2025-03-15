import sqlite3

path=r"D:\MAAB academy new\python\homework\lesson-11\homework\library.db"

with sqlite3.connect(path) as con:
    cursor=con.cursor()
    query="""
    Drop table if exists Library;

    Create table Library(Title text, Author text, Year_published int, Genre text);

    Insert into Library Values('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'), ('1984', '	George Orwell', 1949, 'Dystopian'), ('The Great Gatsby', '	F. Scott Fitzgerald', 1925, 'Classic');

"""
#Creating file
    cursor.executescript(query)

#Updating data
    cursor.execute("UPDATE Library SET Year_published=1950 where title='1984'")

#select 
    select=cursor.execute("SELECT Title, Author from Library where Genre='Dystopian'")
    print(select.fetchall())

#delete
    #cursor.execute("Delete from Library where Year_published<=1950")
    #this will delete data, but didnt do it to keep it for next steps

#bonus task
    update = """
    ALTER table Library ADD column Rating float;

    UPDATE  Library SET Rating=4.8 where Title='To Kill a Mockingbird';
    UPDATE  Library SET Rating=4.7 where Title='1984';
    UPDATE  Library SET Rating=4.5 where Title='The Great Gatsby';

"""
    cursor.executescript(update)
#see all by year_published by acsending order

    all=cursor.execute("Select * from Library order by Year_published asc")
    print(all.fetchall())