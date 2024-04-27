'''
Nama: Naufal Rahfi Anugerah
NIM: 41822010038
'''

# Part B: Mencari Bilangan Ganjil
num = int(input("Enter Number (1-20): "))
if num >= 1 and num <= 20:
  for i in range(0, num):
    if i % 2 == 1:
      print(i*i)
elif num > 20:
  print(f"Number out of range: {num}")
  exit()
elif num < 0:
  print(f"Number cannot Negative: {num}")
  exit()
else:
  print(f"Number cannot zero: {num}")
  exit()
