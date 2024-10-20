meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey.",
            "LOL": "Komik bir şeye verilen cevap.",
            "ROFL" : "Bir şakaya karşılık verilen cevap.",
            "SHEESH" : "Onaylamama ifadesi.",
            "CREEPY" : "Tüyler ürpertici, ürkütücü anlamına gelen söz.",
            "AGGRO" : "Agresifleşmek, sinirlenmek anlamına gelen söz.",
            "OMG" : "Aman tanrım anlamında şaşırma ifadesi.",
            "NGL" : "Gerçekten öyle, yalan söylemiyorum anlamına gelen söz."
            }
word = input("Sözlükten anlamını öğrenmek istediğiniz bir kelimeyi girin: ").upper()

while word not in meme_dict.keys():
    word = input("Lütfen sözlükte olan bir değer girin: ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
