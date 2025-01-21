# numbers = [1,2,3,4,5,6,7,8]
#
# # sq = []
# # for i in number:
# #     sq.append(i ** 2)
# # sq = [number ** 2 for number in numbers]
# # print(sq)
#
# # evens = []
# # for number in numbers:
# #     if number % 2 ==0:
# #         evens.append(number)
# evens = [number for number in numbers if number % 2 == 0]
# print(evens)

# strings = 'python is an awesome language'.split(' ')
#
# filtered = [item for item in strings if len(item) >= 5]
#
# print(filtered)

# sale = {
#     'widget 1': 0,
#     'widget 2': 5,
#     'widget 3': 10,
#     'widget 4': 2
# }
#
# # high_sales = []
# # for key, value in sale.items():
# #     if value >= 5:
# #         high_sales.append(key)
# #         #print(key)
# high_sales = [key for key, value in sale.items() if value >= 5]
# print(high_sales)

# account = [[i + j for j in range(10)] for i in range(50) if i>10]
# print(account)

# widgets = ['widget 1', 'widget 2', 'widget 3', 'widget 4']
# sales = [10,5,15,0]
#
# d = {
#     widgets[i]: sales[i]
#     for i in range(len(widgets))
#     if sales[i] > 0
# }
# print(d)

# widget_sales = [
#     {'name': 'widget 1', 'sales': 10},
#     {'name': 'widget 2', 'sales': 5},
#     {'name': 'widget 3', 'sales': 0}
# ]

#sales_by_widget = {}
# for d in widget_sales:
#     widget_name = d["name"]
#     sale = d['sales']
#     sales_by_widget[widget_name] = sale

# for d in widget_sales:
#      sales_by_widget[d['name']] = d['sales']

# sales_by_widget={d['name']:d['sales'] for d in widget_sales if d['sales']>0}
# print(sales_by_widget)

