import psycopg2
import mapit
import sys

def startDatabase(title):
    try:
        con=psycopg2.connect(database='stockdb', user='postgres',password='football5', host='127.0.0.1')
        print("Opened database successfully")
        cur=con.cursor()
        cur.execute('''CREATE TABLE '''+title+'''
        (ID INT PRIMARY KEY  NOT NULL,
        STOCK   TEXT    NOT NULL,
        PRICE   FLOAT(2)     NOT NULL,
        LIQUID  FLOAT(2)    NOT NULL);''')
        print("Table created successfully")
        con.commit()
        con.close()
    except Exception as e:
        print(e)

def insertData(data, table):
    con=psycopg2.connect(database='stockdb', user='postgres',password='football5', host='127.0.0.1')
    print("Opened database successfully")
    cur=con.cursor()
    i=0
    for stock_name in data:
        i+=1
        stock_symbol="'"+stock_name+"'"
        query="INSERT INTO " + table + " (ID, STOCK, PRICE, LIQUID)\
            VALUES("+ str(i) +", " +stock_symbol+ ", " +str(data[stock_name][1])+ ", " +str(data[stock_name][0])+')'
        print(query)
        cur.execute(query);
    con.commit()
    con.close()
        
def getData(table):
    con=psycopg2.connect(database='stockdb', user='postgres',password='football5', host='127.0.0.1')
    print("Database opened successfully")
    cur=con.cursor()
    cur.execute("SELECT id, stock, price, liquid from "+table)
    rows=cur.fetchall()
    for row in rows:
        print("ID=",row[0])
        print("STOCK=",row[1])
        print("PRICE=",row[2])
        print("LIQUID=",row[3],"\n")
    print("Operation completed successfully")
    con.close()    

def updateData(table, data):
    con=psycopg2.connect(database='stockdb', user='postgres',password='football5', host='127.0.0.1')
    print("Database opened successfully")
    cur=con.cursor()
    i=0
    for stock_name in data:
        i+=1
        stock_symbol="'"+stock_name+"'"
        cur.execute("UPDATE "+table+" set STOCK = "+stock_symbol + ", PRICE = " +str(data[stock_name][1])+",  LIQUID = "+str(data[stock_name][0])+
        "WHERE ID="+str(i))
    con.commit
    print("update complete")
    con.close()

stockdata=mapit.__init__()
#startDatabase('STOCKDATA')
#insertData(stockdata,'STOCKDATA')   
getData('STOCKDATA')
updateData('STOCKDATA', stockdata)
