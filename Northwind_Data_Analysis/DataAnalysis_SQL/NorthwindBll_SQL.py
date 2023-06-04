import pandas as pd
import DataAnalysis_SQL.Queries as Queries
import DataAnalysis_SQL.Connection as Connection

class NorthwindBll: 

    def Get_Customer_Wise_Order_Details(customer_id:int) -> pd.DataFrame:
        conn=Connection.ConnectMySQL()
        get_data1=conn.Get_Dataset(Queries.customer_wise_order_detail.format(customer_id))
        conn.Close_Connection()
        df_customer_wise_order_detail=pd.DataFrame(get_data1,columns=['first_name','last_name','job_title','city','state_province', 'order_id','order_date',
                                                                     'ship_name','ship_city','product_id','quantity','unit_price','product_code','product_name'])
        return df_customer_wise_order_detail
    
    def Get_Monthwise_Highest_Selling_Product() -> pd.DataFrame:
        conn=Connection.ConnectMySQL()
        get_data2=conn.Get_Dataset(Queries.month_wise_highest_sell_product) 
        conn.Close_Connection()
        df_monthwise_highest_selling_product=pd.DataFrame(get_data2, columns=['Y1','M1','product_name','total_quantity','total_price','row_num'])  
        
        return df_monthwise_highest_selling_product  

    def Get_Highest_Ordered_Product() -> pd.DataFrame:
        conn=Connection.ConnectMySQL()
        get_data3=conn.Get_Dataset(Queries.highest_ordered_product)
        conn.Close_Connection()
        df_highest_order_product=pd.DataFrame(get_data3, columns=['product_id','total_quantity','product_name'])
        
        return df_highest_order_product
    
    def Get_Top_5_Customer_Who_Ordered_Most() -> pd.DataFrame:
        conn=Connection.ConnectMySQL()
        get_data4=conn.Get_Dataset(Queries.top_5_customer_who_order_most)
        conn.Close_Connection()
        df_top5_customer_who_order_most=pd.DataFrame(get_data4,columns=['num_order','customer_id','first_name','last_name'])
        
        return df_top5_customer_who_order_most

    def Get_Product_Wise_Monthly_Sell() -> pd.DataFrame:
        conn=Connection.ConnectMySQL()
        get_data5=conn.Get_Dataset(Queries.product_wise_monthly_sell)
        conn.Close_Connection()
        df_pro_wise_mon_sell=pd.DataFrame(get_data5,columns=['month_num','product_name','total_quantity','total_price'])
        
        return df_pro_wise_mon_sell

    def Get_Catagory_Wise_Monthly_Sell() -> pd.DataFrame:
        conn=Connection.ConnectMySQL()
        get_data6=conn.Get_Dataset(Queries.catagory_wise_monthly_sell)
        conn.Close_Connection()
        df_catagory_wise_monthly_sell=pd.DataFrame(get_data6, columns=['category', 'month_num','total_quantity','total_price'])
        
        return df_catagory_wise_monthly_sell

    


