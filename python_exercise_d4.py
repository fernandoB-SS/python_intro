
# List( List(order_number, title_and_author, quantity, price_per), List(...
order_list1 = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung im Python3, Bernd Klein", 3, 24.99]
]


def double_tuple(o_list):
    return map(lambda row: (row[0], row[2] * row[3]), o_list)


for item in double_tuple(order_list1):
    print(item)

 # List( List(order_number, title_and_author, quantity, price_per), List(...
order_list2 = [
    [34587, ("SKU52534", 4, 40.95), ("SKU256126", 10, 12.65)],
    [98762, ("SKU51345", 5, 56.80), ("SKU14515", 3, 32.95)],
    [77226, ("SKU14515", 3, 32.95), ("SKU52534", 4, 40.95)],
    [88112, ("SKU613451", 3, 24.99), ("SKU513461", 6, 26.50)]
]


def order_totaling(o_list):
    result_list = []
    for row in order_list2:
        grand_total = 0
        sub_num = len(row)-1
        for i in range(1, sub_num):
            grand_total += row[i][1] * row[i][2]
            result_list.append((row[0], grand_total))
            return result_list


for item in order_totaling(order_list2):
    print(f"\n{item}")
