# 讀取檔案
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續
		name, price = line.strip().split(',')  #strip去掉多餘空格或換行符號; split使用逗點做切割
		products.append([name, price])
print(products)

# 讓使用者輸入
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

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w') as f:  		#with 就是自動close; encoding最廣泛使用編碼，避免亂碼
	f.write('商品,價格\n')  					#欄位名稱
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')   #csv檔都會用逗點來換格
											# int為轉整數 , str為轉字串


