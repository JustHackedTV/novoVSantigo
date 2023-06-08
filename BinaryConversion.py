inputs = input('>>> ')
	
def deocode_new(binary):
	sequence = list(binary)
	number = 0
	for i in range(len(sequence)):
		number += pow(2, i)*int(sequence[-(i+1)])
	try:
		print(f"{number} {chr(number+96).upper()}")
	except OverflowError:
		print(f"{number}")

def decode_old(bin):
  Binario=bin
  if Binario=="00000":
    print("0 (espaço)")
  elif Binario=="00001":
    print("1 A")
  elif Binario=="00010":
    print("2 B")
  elif Binario=="00011":
    print("3 C")
  elif Binario=="00100":
    print("4 D")
  elif Binario=="00101":
    print("5 E")
  elif Binario=="00110":
    print("6 F")
  elif Binario=="00111":
    print("7 G")
  elif Binario=="01000":
    print("8 H")
  elif Binario=="01001":
    print("9 I")
  elif Binario=="01010":
    print("10 J")
  elif Binario=="01011":
    print("11 K")
  elif Binario=="01100":
    print("12 L")
  elif Binario=="01101":
    print("13 M")
  elif Binario=="01110":
    print("14 N")
  elif Binario=="01111":
    print("15 O")
  elif Binario=="10000":
    print("16 P")
  elif Binario=="10001":
    print("17 Q")
  elif Binario=="10010":
    print("18 R")
  elif Binario=="10011":
    print("19 S")
  elif Binario=="10100":
    print("20 T")
  elif Binario=="10101":
    print("21 U")
  elif Binario=="10110":
    print("22 V")
  elif Binario=="10111":
    print("23 W")
  elif Binario=="11000":
    print("24 X")
  elif Binario=="11001":
    print("25 Y")
  elif Binario=="11010":
    print("26 Z")
  else:
    print("Binario invalido!")

decode_old(inputs)
deocode_new(inputs)