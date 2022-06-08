status = str(input("status = "))
jumlah_lembar = int(input("jumlah lembar = "))

if(status == "langganan"):
	total_bayar = jumlah_lembar * 100
	print("total_bayar",total_bayar)
elif(status == "bukan langganan"):
	if(jumlah_lembar < 100):
		total_bayar = jumlah_lembar * 150
	else:
		total_bayar = jumlah_lembar * 125
		
	print("total_bayar",total_bayar)

else:
	print("input tidak valid")