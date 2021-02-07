import sys
import os

def Encode(data):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    bit_str = ""
    base64_str = ""

    for char in data:
        bin_char = bin(char).lstrip("0b")
        bin_char = bin_char.zfill(8)
        bit_str += bin_char

    brackets = [bit_str[x:x+6] for x in range(0,len(bit_str),6)]

    for bracket in brackets:
        if(len(bracket) < 6):
            bracket = bracket + (6-len(bracket))*"0"
        base64_str += alphabet[int(bracket,2)]

    padding_indicator = len(base64_str) % 4
    if padding_indicator == 3:
        base64_str += "="
    elif  padding_indicator == 2:
        base64_str += "=="

    return base64_str

def base64Encode(inFile, outFile):
    with open(outFile, "w") as w:
        with open(inFile, "rb") as f:
            byte = f.read(57)
            while byte:
                w.write(Encode(byte))
                w.write("\n")
                byte = f.read(57)

file_name = sys.argv[1]

base64Encode(file_name, file_name + "out.txt")
print(f"Outputed to file {file_name}out.txt")