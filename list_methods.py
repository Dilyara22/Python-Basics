fruits=['orange','apple','pear']
vegetables=['carrot','potato','onion']
final_shopping_list=fruits+vegetables
print(final_shopping_list)
print(len(final_shopping_list))
final_shopping_list.append('cabbage')
print(final_shopping_list)
final_shopping_list.pop()
print(final_shopping_list)

sweets=['chocolate','cake','candy']
final_shopping_list.extend(sweets)
print(final_shopping_list)

final_shopping_list.remove('apple')
print(final_shopping_list)

print(list('Dilyara'))

customer_info='Mike|Canada|30|Male'
print(customer_info.split('|'))

