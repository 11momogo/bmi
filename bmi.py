height = input('請輸入身高(公分): ')
weight = input('請輸入體重(公斤): ')
h = float(height) / 100 # 公分轉公尺
w = float(weight)

bmi = w / h ** 2

if bmi < 18.5:
	print('您的bmi值為 ', bmi, '屬於體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('您的bmi值為 ', bmi,'屬於體重正常')
elif bmi >=24 and bmi < 27:
	print('您的bmi值為 ', bmi,'屬於體重過重')
elif bmi >=27 and bmi <= 30:
	print('您的bmi值為 ', bmi,'屬於輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('您的bmi值為 ', bmi,'屬於中度肥胖')
else: # 也可以用 elif
	print('您的bmi值為 ', bmi,'屬於重度肥胖')
