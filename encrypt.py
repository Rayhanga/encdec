from Encryption import main

if __name__ == "__main__":
	p = input("Plain Text: ")
	k = input("Key: ")

	enc = main.encrypt(p, k)

	if(enc):
		print('Encrypted Message: {}'.format(enc))
