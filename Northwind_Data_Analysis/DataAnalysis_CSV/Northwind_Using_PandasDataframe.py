import pandas as pd
import Northwind_Dataframe

class Northwind_PandasDataframe:
    def Get_Customer_Detail():
        df_Customer=Northwind_Dataframe.Northwind_PdDataframe.Get_Customer_Dataframe()
        return df_Customer
    # 1. Find highest ordered product
    def Get_Highest_Ordered_Product() -> pd.DataFrame:
        
        df_Products=Northwind_Dataframe.Northwind_PdDataframe.Get_Products_Dataframe()
        df_Order_Detail=Northwind_Dataframe.Northwind_PdDataframe.Get_Order_Detail_Dataframe()
        df_Order_Detail=df_Order_Detail[['order_id','product_id', 'quantity','unit_price']]
        df_Products=df_Products[['id','product_name']]
        new_df= pd.merge(df_Order_Detail, df_Products, left_on='product_id', right_on='id')
        new_df.drop('id', axis=1, inplace=True)

        return new_df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(1)
    
    # 2. Find top 5 customers who ordered most

    def Get_Top_5_Customer_Who_Ordered_Most():
      
        df_Customer=Northwind_Dataframe.Northwind_PdDataframe.Get_Customer_Dataframe()
        df_Order=Northwind_Dataframe.Northwind_PdDataframe.Get_Order_Dataframe()
        df_Customer=df_Customer[['id','first_name','last_name']]
        df_Customer['customer_name']=df_Customer['first_name']+ ' '+ df_Customer['last_name']
        df_Order=df_Order[['id','customer_id','order_date']]
        df_Order.rename(columns={'id':'order_id'},inplace=True)
        new_df=pd.merge(df_Order,df_Customer,left_on='customer_id',right_on='id')
        new_df.drop('id',axis=1, inplace=True)
        return new_df.groupby('customer_name')['order_id'].count().sort_values(ascending=False).head(5)

    # 3. Show all products ordered by one customer
    
    def Get_All_Products_Ordered_By_Customer(customer_id:int)-> None:
        
        df_Customer=Northwind_Dataframe.Northwind_PdDataframe.Get_Customer_Dataframe()
        df_Order=Northwind_Dataframe.Northwind_PdDataframe.Get_Order_Dataframe()
        df_Order_Detail=Northwind_Dataframe.Northwind_PdDataframe.Get_Order_Detail_Dataframe()
        df_Products=Northwind_Dataframe.Northwind_PdDataframe.Get_Products_Dataframe()
        df_Customer=df_Customer[['id','first_name','last_name']]
        df_Customer['customer_name']=df_Customer['first_name']+ ' '+ df_Customer['last_name']
        df_Order=df_Order[['id','customer_id','order_date']]
        df_Order.rename(columns={'id':'order_id'},inplace=True)
        new_df=pd.merge(df_Order,df_Customer,left_on='customer_id',right_on='id')
        new_df.drop(columns=['id','first_name','last_name'], axis = 1, inplace = True)
        df_Order_Detail=df_Order_Detail[['order_id','product_id','quantity','unit_price']]
        df_Order_Detail['total_price']=df_Order_Detail['quantity'] * df_Order_Detail['unit_price']
        new_df1=pd.merge(new_df,df_Order_Detail,on='order_id')
        df_Products=df_Products[['id','product_name','category']]
        final_df=pd.merge(new_df1,df_Products,left_on='product_id',right_on='id')
        final_df.drop(['id'], axis = 1, inplace = True)
        products_ordered_by_customer_df=final_df[final_df['customer_id']==customer_id]
        return products_ordered_by_customer_df[['customer_name','product_name','category','quantity','unit_price','total_price']]
        
    # 4. Monthly highest selled product 
    def Show_Monthwise_Highest_Selling_Product(month_name:str)-> None:
        
        df_Customer=Northwind_Dataframe.Northwind_PdDataframe.Get_Customer_Dataframe()
        df_Order=Northwind_Dataframe.Northwind_PdDataframe.Get_Order_Dataframe()
        df_Order_Detail=Northwind_Dataframe.Northwind_PdDataframe.Get_Order_Detail_Dataframe()
        df_Products=Northwind_Dataframe.Northwind_PdDataframe.Get_Products_Dataframe()   
        df_Customer=df_Customer[['id','first_name','last_name']]
        df_Customer['customer_name']=df_Customer['first_name']+ ' '+ df_Customer['last_name']
        df_Order=df_Order[['id','customer_id','order_date']]
        df_Order.rename(columns={'id':'order_id'},inplace=True)
        new_df=pd.merge(df_Order,df_Customer,left_on='customer_id',right_on='id')
        new_df.drop(columns=['id','first_name','last_name'], axis = 1, inplace = True)
        df_Order_Detail=df_Order_Detail[['order_id','product_id','quantity','unit_price']]
        df_Order_Detail['total_price']=df_Order_Detail['quantity'] * df_Order_Detail['unit_price']
        new_df1=pd.merge(new_df,df_Order_Detail,on='order_id')
        df_Products=df_Products[['id','product_name','category']]
        final_df=pd.merge(new_df1,df_Products,left_on='product_id',right_on='id')
        final_df.drop(['id'], axis = 1, inplace = True)
        final_df['order_date'] = pd.to_datetime(final_df['order_date'])
        final_df['day'] = final_df['order_date'].dt.day
        final_df['month'] = final_df['order_date'].dt.month_name()
        final_df['year'] = final_df['order_date'].dt.year
        monthly_sell_product=final_df[final_df['month'] == month_name]
        return monthly_sell_product.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(1)

    # 5. Find monthly highest selling product catagory wise

    def Show_Monthwise_Highest_Selling_Product_Categorywise(month_name:str)-> None:
        
        df_Customer=Northwind_Dataframe.Northwind_PdDataframe.Get_Customer_Dataframe()
        df_Order=Northwind_Dataframe.Northwind_PdDataframe.Get_Order_Dataframe()
        df_Order_Detail=Northwind_Dataframe.Northwind_PdDataframe.Get_Order_Detail_Dataframe()
        df_Products=Northwind_Dataframe.Northwind_PdDataframe.Get_Products_Dataframe()   
        df_Customer=df_Customer[['id','first_name','last_name']]
        df_Customer['customer_name']=df_Customer['first_name']+ ' '+ df_Customer['last_name']
        df_Order=df_Order[['id','customer_id','order_date']]
        df_Order.rename(columns={'id':'order_id'},inplace=True)
        new_df=pd.merge(df_Order,df_Customer,left_on='customer_id',right_on='id')
        new_df.drop(columns=['id','first_name','last_name'], axis = 1, inplace = True)
        df_Order_Detail=df_Order_Detail[['order_id','product_id','quantity','unit_price']]
        df_Order_Detail['total_price']=df_Order_Detail['quantity'] * df_Order_Detail['unit_price']
        new_df1=pd.merge(new_df,df_Order_Detail,on='order_id')
        df_Products=df_Products[['id','product_name','category']]
        final_df=pd.merge(new_df1,df_Products,left_on='product_id',right_on='id')
        final_df.drop(['id'], axis = 1, inplace = True)
        final_df['order_date'] = pd.to_datetime(final_df['order_date'])
        final_df['day'] = final_df['order_date'].dt.day
        final_df['month'] = final_df['order_date'].dt.month_name()
        final_df['year'] = final_df['order_date'].dt.year
        monthly_sell_product=final_df[final_df['month'] == month_name]
        return monthly_sell_product.groupby('category')['quantity'].sum().sort_values(ascending=False).head(1)
    

#print(Northwind_PandasDataframe.Get_Highest_Ordered_Product())
#print(Northwind_PandasDataframe.Get_Top_5_Customer_Who_Ordered_Most())
#print(Northwind_PandasDataframe.Get_All_Products_Ordered_By_Customer(3))
#print(Northwind_PandasDataframe.Show_Monthwise_Highest_Selling_Product('February'))
#print(Northwind_Dataframe.Northwind_PdDataframe.Get_Customer_Dataframe())
#print(Northwind_PandasDataframe.Show_Monthwise_Highest_Selling_Product_Categorywise('March'))