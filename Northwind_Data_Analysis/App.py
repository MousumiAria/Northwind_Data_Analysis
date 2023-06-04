import DataAnalysis_SQL.NorthwindBll_SQL as NB_SQL
import pandas as pd


class DataframeUtil:
    def Write_Dataframe_To_CSV(df:pd.DataFrame, path:str) -> None:
        df_generic= df
        df_generic.to_csv(path)
 
 
# print(NorthwindBll.NorthwindBll.Get_Customer_Wise_Order_Details(7))

DataframeUtil.Write_Dataframe_To_CSV(NB_SQL.NorthwindBll.Get_Customer_Wise_Order_Details(4),'CSV\customer_wise_ordered_details1.csv')