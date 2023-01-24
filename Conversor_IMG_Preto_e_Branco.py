from PIL import Image

# Nessta parte você carrega a Imagem
img_file = Image.open(r'.\Fotos\img.jpg')

# Imagem convertida para Preto e Branco
img_file = img_file.convert('L')

# Salva a Imagem no caminho selecionado
img_file.save(r'.\Fotos\preto_e_banco.png')
