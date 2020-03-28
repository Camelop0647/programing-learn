import pandas as pd
import numpy as np
import math

def calc_credit_management_level(base_val, post_val):
    total_salary =base_val+post_val
    social_insurance = round(total_salary * 0.18, -1)
    income_tax = (total_salary - social_insurance) *0.10
    credit =total_salary - social_insurance - income_tax 
    return credit

def calc_credit_non_management_level(base_val, over_time):
    over_time_salary = math.floor(over_time * round(base_val / 160 *1.25, -1) /10) *10
    total_salary = base_val + over_time_salary
    social_insurance = round(total_salary * 0.18, -1)
    income_tax = (total_salary - social_insurance) *0.10
    credit = total_salary - social_insurance -income_tax
    return credit

def calc_credit_part_timer(time_rate, work_time):
    total_salary = time_rate * work_time
    income_tax = total_salary * 0.1
    credit = total_salary - income_tax
    return credit

if __name__ == "__main__":
    col_list= ["name","type", "base_val", "post_val", "over_time", "time_rate","work_time"]
    df = pd.DataFrame(columns=col_list)
    temp_df= pd.DataFrame(np.array([["寺尾哲雄","manager",350000,80000,0,0,0],
                                    ["若林仁継","manager",375000,40000,0,0,0],
                                    ["寺田帆香","non_manager",320000,0,30,0,0],
                                    ["広田康博","non_manager",295000,0,20,0,0],
                                    ["菅沼洋一郎","non_manager",220000,0,35,0,0],
                                    ["菊地章","part_time",0,0,0,1200,90],
                                    ["山岸柑奈","part_time",0,0,0,1000,120],
                                    ["望月由文","part_time",0,0,0,1100,90]
                                    ]
                                    ))
    temp_df.columns= col_list
    df =df.append(temp_df)
    #なぜかstr型で認識されるため、型変換
    convert_col_name = ["base_val", "post_val", "over_time", "time_rate","work_time"]
    for temp_col_name in convert_col_name:
        temp_df[temp_col_name] = temp_df[temp_col_name].astype(int)

    #給与計算をif文で書いて出力
    for i in range(len(df)):
        temp_indivisual_info = temp_df.iloc[i]
        # print(temp_indivisual_info)
        if temp_indivisual_info["type"] == "manager":
            print(f"{temp_indivisual_info['name']} :",calc_credit_management_level(temp_indivisual_info['base_val'], temp_indivisual_info['post_val']))
        elif temp_indivisual_info["type"] == "non_manager":
            print(f"{temp_indivisual_info['name']} :",calc_credit_non_management_level(temp_indivisual_info['base_val'], temp_indivisual_info['over_time']))
        elif temp_indivisual_info["type"] == "part_time":
            print(f"{temp_indivisual_info['name']} :",calc_credit_part_timer(temp_indivisual_info['time_rate'], temp_indivisual_info['work_time']))