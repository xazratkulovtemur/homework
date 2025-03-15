import sqlite3
path=r"D:\MAAB academy new\python\homework\lesson-11\homework\roster.db"
#Creating the table
with sqlite3.connect(path) as con:
    cursor=con.cursor()

    query="""
        Drop table if exists Roster;
        Create table Roster(Name text, Species text, age int);
        Insert into Roster Values('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)
    
"""
    cursor.executescript(query)

    #Updating the table
    cursor.execute("UPDATE Roster SET name='Ezri Dax' WHERE age=300")
#Display name and Age
    data=cursor.execute("Select Name, age from Roster where species='Bajoran'")
    print(data.fetchall())
#deleting info for age>100
    cursor.execute("Delete from Roster where age>100")

    

#adding new column
    rank = """
    ALTER TABLE Roster ADD COLUMN Rank TEXT;

    UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko';
    UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys';
""" 
    cursor.executescript(rank)

    #all by age in descending order
    all=cursor.execute("Select * from  Roster order by age desc")
    print(all.fetchall())
   

    



