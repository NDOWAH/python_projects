orders = [
    [34587,'Learning Python',4,40.95],
    [98762,'Mark Lutz Programming Python',5,56.80],
    [77226,'Mark Lutz Head First Python',3,32.95],
    [88112,'Paul Barry Einführung in Python3',3,24.99]
]
min_order = 100
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), 
                  map(lambda x: (x[0],x[2] * x[3]), orders)))
print(invoice_totals)