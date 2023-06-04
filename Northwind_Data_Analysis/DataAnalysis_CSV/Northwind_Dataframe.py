import pandas as pd
import os

class Northwind_PdDataframe:

    def Get_Customer_Dataframe()-> pd.DataFrame:
        path="E:\\Mou_Projects\\Northwind_CSV_File\\Customer.csv"
        return pd.read_csv(path)
    
    def Get_Employee_Dataframe()-> pd.DataFrame:
        path="E:\\Mou_Projects\\Northwind_CSV_File\\Employee.csv"
        return pd.read_csv(path)
    
    def Get_Products_Dataframe()-> pd.DataFrame:
        path="E:\\Mou_Projects\\Northwind_CSV_File\\Products.csv"
        return pd.read_csv(path)
    
    def Get_Order_Detail_Dataframe()-> pd.DataFrame:
        path="E:\\Mou_Projects\\Northwind_CSV_File\\Order_Detail.csv"
        return pd.read_csv(path)
    
    def Get_Order_Dataframe()-> pd.DataFrame:
        path="E:\\Mou_Projects\\Northwind_CSV_File\\Order.csv"
        return pd.read_csv(path)
    
# print(Northwind_PdDataframe.Get_Products_Dataframe())