num_dictnry = {
    'Row 1': [1]
}

num_list = [1,2,3] #Look and Say Pyramid never has more than 3 distinct numbers

pyrmd_height = round(float(input("Input a integer between 1 to 10 ")),0)

rows = 1
count = 0

while pyrmd_height != rows:
    num_dictnry[f'Row {rows + 1}'] = []
    counted_num = None
    for i,num in enumerate(num_dictnry[f'Row {rows}']):
        for b in num_list:
            if num == b:
                count += 1
        counted_num = num
        try:
            if num_dictnry[f'Row {rows}'][i+1] != num:
                num_dictnry[f'Row {rows + 1}'].extend([count,counted_num])
                count = 0
        except IndexError:
            continue
    num_dictnry[f'Row {rows + 1}'].extend([count,counted_num])
    count = 0
    rows += 1

print(num_dictnry)
