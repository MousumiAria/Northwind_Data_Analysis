import mysql.connector

class ConnectMySQL:
       
    def __init__(self):
        self.__cnx = None
        self.__Connect_to_DB()

    
    def __Connect(self):
        return mysql.connector.connect(user='root', password='mousen@1983',
                host='localhost',
                database='northwind')
    
    def __Connect_to_DB(self) -> None:              
        if self.__cnx is None:   
            self.__cnx =self.__Connect() 
    
    def Get_Dataset(self,str_query:str):
        mycursor = self.__cnx.cursor()
        mycursor.execute(str_query)
        myresult = mycursor.fetchall()
        return myresult
    
    def Close_Connection(self) -> None:
        self.__cnx.close()
    
    
