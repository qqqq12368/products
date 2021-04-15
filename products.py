products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	# p = []    第一種
	# p.append(name)
	# p.append(price)
	# p = [name, price] 第二種
	# products.append(p)
	products.append([name, price])
print(products)

