

def baiduTableFormat(response:dict)->list:
    print(response)
    maxRow = 0
    maxColum =0
    #找到最大行列
    for item in response["tables_result"][0]["body"]:
        if item["row_start"] > maxRow:
            maxRow = item["row_start"]
        if item["col_start"] > maxColum:
            maxColum = item["col_start"]
        if item["row_end"] > maxRow:
            maxRow = item["row_end"]
        if item["col_end"] > maxColum:
            maxColum = item["col_end"]
    table = [[None]*(maxColum+1) for i in range(maxRow+1)]

    for item in response["tables_result"][0]["body"]:
        table[item["row_start"]][item["col_start"]] = item["words"]
        
    return table



