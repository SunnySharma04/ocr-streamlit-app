import easyocr as ocr  #OCR

reader = ocr.Reader(['en','hi'],model_storage_directory='.')

result = reader.readtext("outliers.jpeg")

for text in result:
    print(text[1])