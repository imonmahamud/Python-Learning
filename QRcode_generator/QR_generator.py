import qrcode

# text=input('Enter the text to convert qr code : ')

# filename= input('Enter the filename to save the qr code : ')


# def generate_qr_code(filepath):    
#     with open(filepath, 'r') as file:
#         lines=file.readlines()
#     text=lines[0].strip()
#     filename=lines[1].strip()
    
        
    
#     generate_qrcode= qrcode.make(text)
#     generate_qrcode.save(filename)

# generate_qr_code('input.txt')

with open('input1.txt', 'r') as file:
    # file.write('https:www.facebook.com\n')
    # file.write('facebook.png')
    lines=file.readlines()

text=lines[0].strip()
filename=lines[1].strip()

qr=qrcode.make(text)
qr.save(filename)

    
