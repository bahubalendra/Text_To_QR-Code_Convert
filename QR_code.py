#it's work
import pyqrcode

'''
data = 'Bahubalendra Barik'
img = pyqrcode.create(data)
img.png('BB.png', scale=10)
'''
def qrcode():
    q=pyqrcode.create(input("Enter your Text..."))
    q.png('Bahubalendra.png', scale=5)
    print("QR generated")

if __name__=='__main__':
    qrcode()