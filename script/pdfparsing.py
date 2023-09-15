import pdfplumber
import pandas as pd
import re

# PDF dosyasının yolunu belirtiyoruz.
pdf_path = "parsepdf.pdf"

# PDF dosyasını aç ve metni pdf içerisinden çıkar
with pdfplumber.open(pdf_path) as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

# Elimizde belirli bir düzeni ve kuralı olmayan metinler var bunların içerisinden ayıklama yapmak için
# kullanacağımız regular expression düzeni
pattern = r'Bk\. (\d+) (.+?)(?=\nBk\. \d+|\Z)'
matches = re.findall(pattern, text, re.DOTALL)

# Verileri pandas ile düzenliyoruz ve DataFrame'e dönüştürüyoruz. böylece daha düzgün bir tablo yapısı oluşacak.
data = {'Bk Numarası': [], 'İçerik Metin': []}
for match in matches:
    bk_numarasi = match[0]
    bk_metni = match[1].strip()
    data['Bk Numarası'].append("Bk. " +bk_numarasi)
    data['İçerik Metin'].append(bk_metni)

df = pd.DataFrame(data)

# Elde ettiğimiz DataFrame'i Excel dosyasına kaydediyoruz.
excel_output_path = "pdfparse.xlsx"
df.to_excel(excel_output_path, index=False)
