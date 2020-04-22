#密碼重試程式
#
#在設定預設密碼 password = "a1234"
#使用者最多輸入3次密碼
#不對就顯示出"密碼錯誤!還有_次機會"
#對的話顯示出"登入成功"

password = 'a1234'
i = 2
while i >= 0 :
	try_password = input('請輸入密碼')
	if try_password == password :
		print('登入成功')
		break
	else :
		if i == 0 :
			print('密碼錯誤!您已經沒有輸入機會')
			break
		print('密碼錯誤!還有', i, '次機會')
		i = i - 1
	    