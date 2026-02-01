import qrcode
from urllib.parse import urlparse
import os

#A basic qrcode generator with a custom saving strategy of parsing through the url and saving it using the domain name 
url=input("Enter a url: ").strip()
folder=r"C:\Users\user\Desktop\Projects\PY\Projects\Qr_code_images"

parsed=urlparse(url)
#checks the url for the netloc and gives as the domain name if no protocol ,
#  it splits the url and give the first chunk as the domain 
domain=parsed.netloc or parsed.path.split('/')[0] 
clean_url=domain.replace(":","_")

file_path=os.path.join(folder,f"{clean_url}.png")

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)