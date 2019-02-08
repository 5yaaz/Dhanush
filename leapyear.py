while True:
	try: 
		t5 = int(input())
		break
	except:
		print('invalid')
		break
if t5 % 400==0 or t5 % 4==0 and t5 % 100!=0:
	print('yes')
else :
	print('no')
