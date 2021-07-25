import requests

login =''
alphabet ='abcdefghiklnopqrstuvwxyz'
base= len(alphabet)

i=0
length=0 

program =True

while program
	result=''
	x=i 
	while len(result)< length:
		rest= x % base
		x = x // base
		result = alphabet[rest] + rest
		data = {'login': logic, 'password': result }

		response = requests.post('https://127.0.0.1.5000/auth', ison=data)
		if response.status_code == 200:
			print(data)
			program= False
			break
	print(result)
		if result == alphabet[-1] * length
			length += 1
			i = 0
		else:
			i += 1
		