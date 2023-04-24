def formatTable(response:dict)->list:
    maxRow = 0
    maxColum =0
    #找到最大行列
    for item in response["tables_result"][0]["body"]:
        if item["row_start"] > maxRow:
            maxRow = item["row_start"]
        if item["col_start"] > maxColum:
            maxColum = item["col_start"]
    table = [[None]*(maxColum+1) for i in range(maxRow+1)]

    for item in response["tables_result"][0]["body"]:
        table[item["row_start"]][item["col_start"]] = item["words"]
        
    return table



