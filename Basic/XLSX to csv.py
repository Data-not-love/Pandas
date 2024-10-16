import pandas as pd

#Đọc file excel vói đường dẫn chưa chưa đổi \ =>/
input_excel = input("Must end with .xlsx and use complete path: ")

def reformat_path (str):
    re_format_input = ""
    for char in str:
        if char == "\\" :
            re_format_input += "/"
        else :
            re_format_input += char
        if len(str) == len(re_format_input):
            return re_format_input



new_format = reformat_path(input_excel)
excel = pd.read_excel(new_format)
excel = excel.fillna('NaN')

input_save_location = input("Use complete path for better accuracy : ")
save_reformat = reformat_path(input_save_location)
to_csv = excel.to_csv(save_reformat, index=False) # để ko in thuộc tính đầu sau dấu ,