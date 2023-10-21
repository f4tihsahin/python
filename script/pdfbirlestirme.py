import os
import fitz
import shutil
 
klasor1 = 'C:\\Users\\user\\Desktop\\pythonpdf\\klasör1'
klasor2 = 'C:\\Users\\user\\Desktop\\pythonpdf\\klasör2'
hedef_klasor = 'C:\\user\\user\\Desktop\\pythonpdf\\hedef_klasör'

# Hedef klasörü oluşturun (eğer yoksa)
if not os.path.exists(hedef_klasor):
    os.makedirs(hedef_klasor)


def birlestir_ve_tasi(pdf_ad):
    yol_klasor1 = os.path.join(klasor1, pdf_ad)
    yol_klasor2 = os.path.join(klasor2, pdf_ad)
    hedef_yol = os.path.join(hedef_klasor, pdf_ad)

    pdf_birlestirici = fitz.open()

    if os.path.exists(yol_klasor1):
        pdf1 = fitz.open(yol_klasor1)
        pdf_birlestirici.insert_pdf(pdf1)

    if os.path.exists(yol_klasor2):
        pdf2 = fitz.open(yol_klasor2)
        pdf_birlestirici.insert_pdf(pdf2)

    pdf_birlestirici.save(hedef_yol)
    pdf_birlestirici.close()

    print(f'{pdf_ad} birleştirilip {hedef_klasor} klasörüne taşındı.')


# Klasör 1'deki PDF dosyalarını işle
for pdf_dosya in os.listdir(klasor1):
    if pdf_dosya.endswith('.pdf'):
        birlestir_ve_tasi(pdf_dosya)

# Klasör 2'deki PDF dosyalarını işle
for pdf_dosya in os.listdir(klasor2):
    if pdf_dosya.endswith('.pdf'):
        if pdf_dosya not in os.listdir(hedef_klasor):
            # Eğer hedef klasörde aynı isimde bir dosya yoksa, kopyala
            shutil.copyfile(os.path.join(klasor2, pdf_dosya), os.path.join(hedef_klasor, pdf_dosya))
            print(f'{pdf_dosya} hedef klasöre kopyalandı.')