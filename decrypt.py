from Encryption import main

if __name__ == "__main__":
	p = input("Encrypted Message: ")
	k = input("Key: ")

	dec = main.decrypt(p, k)

	if(dec):
		print('Decrypted Message: {}'.format(dec))
