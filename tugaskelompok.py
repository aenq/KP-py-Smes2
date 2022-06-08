print ('==========//SELAMAT DATANG//==========')

print (' ')

print ('program menghitung luas bangun datar')

print (' ')

while True:
  print('//silahkan pilih menu yang tersedia//')
  print('pilihan menu :\n 1. persegi panjang\n 2. persegi\n 3. segitiga\n 4. trapesium\n 5. jajargenjang\n 6. belah ketupat\n 7. lingkaran\n 8. exit\n')

  pilih = float(input('masukkan pilihan anda (dalam angka) :', ))
  if pilih == 1:
      print('pilihan anda adalah persegi panjang')

      print(' ')

      print('rumus luas = panjang x lebar')
      a = float(input('masukkan panjang (cm) ='))
      b = float(input('masukkan lebar (cm) ='))
      l = a * b
      
      print(' ')
      
      print('luas persegi panjang adalah %.f' %l, 'cm²')
      
      print (' ')
      
  elif pilih == 2:
      print('pilihan anda adalah persegi')
      
      print(' ')
      
      print ('rumus luas = sisi x sisi')
      s = float(input('masukkan panjang sisi (cm) ='))
      l = s * s
      
      print(' ')
      
      print('luas persegi adalah %.f' %l, 'cm²')
      
      print (' ')
      
  elif pilih == 3:
      print('pilihan anda adalah segitiga')
      
      print (' ')
      
      print ('rumus luas = ( alas x tinggi ) / 2')
      a = float(input('masukkan panjang alas (cm) ='))
      t = float(input('masukkan nilai tinggi (cm) ='))
      l = (a*t)/2
      
      print(' ')
      
      print('luas segitiga adalah %.f' %l, 'cm²')
      
      print (' ')
      
  elif pilih == 4:
      print('pilihan anda adalah trapesium')
      
      print (' ')
      
      print ('rumus luas = ( sisi atas + sisi bawah ) x tinggi/2 ')
      a = float(input('masukkan panjang sisi atas (cm) ='))
      b = float(input('masukkan panjang sisi bawah (cm) ='))
      t = float(input('masukkan nilai tinggi (cm) ='))
      l = (a+b) * t/2
      
      print(' ')
      
      print('luas trapesium adalah %.f' %l, 'cm²')
      
      print (' ')
      
  elif pilih == 5:
      print('pilihan anda adalah jajargenjang')
      
      print(' ')
      
      print ('rumus luas = alas x tinggi')
      a = float(input('masukkan panjang alas (cm) ='))
      t = float(input('massukkan nilai tinggi (cm) ='))
      l = a * t
      
      print(' ')
      
      print('luas jajargenjang adalah %.f' %l, 'cm²')
      
      print(' ')
      
  elif pilih == 6:
      print('pilihan anda adalah belah ketupat')
      
      print(' ')
      
      print('rumus luas = (diagonal 1 x diagonal 2) /2')
      d1 = float(input('masukkan panjang diagonal satu (cm) ='))
      d2 = float(input('masukkan panjang diagonal dua (cm) ='))
      l = (d1 * d2)/2
      
      print(' ')
      
      print('luas belah ketupat adalah %.f' %l, 'cm²')
      
      print(' ')
      
  elif pilih == 7:
      print('pilihan anda adalah lingkaran')
      
      print(' ')
      
      print('rumus luas = phi x jari-jari x jari-jari')
      phi = 3.14
      r = float(input('masukkan panjang jari-jari (cm) ='))
      l = phi * r * r
      
      print(' ')
      
      print('luas lingkaran adalah %.f' %l, 'cm²')
      
      print('')
      
  elif pilih == 8:
      print('======//TERIMAKASIH//======')
      break
  else:
      print('!!! INPUT YANG ANDA MASUKKAN TIDAK VALID !!!')
      break