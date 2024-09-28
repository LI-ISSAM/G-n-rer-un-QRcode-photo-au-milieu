import qrcode # module nécessaire pour creer un QRCODE
from PIL import Image,ImageDraw # module pour jouer et modifier les images

Qr = qrcode.QRCode(
    version = 7, # il existe environ '40' version , vous pouvez les essayer
    error_correction = qrcode.ERROR_CORRECT_L, # s'il y'a des erreur on utilse la correction pour les diminuer et la version _L et le plus bas
    box_size = 8, # taille de boite
    border = 2 # frontiére
)

Qr.add_data('Vos informations .....') # inserer votre donnée que ce soit lien d'instagram ou whatsapp , etc....
Qr.make(fit=True) , # on assure bien que notre QR sera manipuler
image = Qr.make_image(back_color = 'white',fill_color = 'black').convert('RGB') # reglage des couleur de note QR

photo = Image.open('yeux.jpg') # attribuer ta photo à la variable 'photo'
taille_photo = int(image.size[0] *.25) # vous pouvez preciser la taille de votre image que vous le souhaiter
photo = photo.resize((taille_photo,taille_photo)) # redimensionner  la photo


masque = Image.new('L',(taille_photo,taille_photo),0) # 'L' veut dire couleur grise ,entre () on met la taille de la photo , 0 => couleur noir
dessiner = ImageDraw.Draw(masque) # on fait cette etape pour qu'on puisse jouer et modifier le masque comme on veut,pour dessiner un rectangle,un circle,text,.....
dessiner.ellipse((0,0,taille_photo,taille_photo),fill = 'white') # ellipse veut dire 'circle'

xq = int (image.size[0]/2) # pour size[0] represente la largeur de la photo
yq = int (image.size[1]/2) # pour size[1] représente la hauteur de la photo
photo.x = xq 
photo.y = yq
pos = (photo.x-int(photo.size[0]/2),photo.y-int(photo.size[1]/2)) # on'a fait ce calcule pour positionner notre photo au milieu de l'image


image.paste(photo,pos,mask = masque) # appliquer la photo sur l'image de QRCODE 
image.save('QR-professionel.png') # enregisterement de l'image