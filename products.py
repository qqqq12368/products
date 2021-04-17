import os # operating system


# 讀取檔案+確認檔案是否存在
def read_file(filename):
	products = []
	if os.path.isfile(filename):
		print('ya')
		with open(filename, 'r') as f:
			for line in f:
				if '商品,價格' in line:
					continue #繼續
				name, price = line.strip().split(',')  #strip去掉多餘空格或換行符號; split使用逗點做切割
				products.append([name, price])
		print(products)
	else:
		print('no')
	return products


# 讓使用者輸入
def user_input(products):
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
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:  		#with 就是自動close; encoding最廣泛使用編碼，避免亂碼
		f.write('商品,價格\n')  					#欄位名稱
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')   #csv檔都會用逗點來換格
												# int為轉整數 , str為轉字串


products = (read_file('products.csv'))
products = (user_input(products))
print_products(products)
write_file('products.csv', products)


