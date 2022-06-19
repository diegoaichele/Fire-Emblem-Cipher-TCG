import requests , os, sqlite3, time
from bs4 import BeautifulSoup

def download_img(card_image_url,card_code):
  r = requests.get(card_image_url)
  with open(os.path.join("images",card_code + ".png"), 'wb') as f:
          f.write(r.content)


con = sqlite3.connect('cipher_fireemblem.db')
cur = con.cursor()

insert_card = "INSERT INTO card VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
insert_affinities = "INSERT INTO affinities VALUES (?, ? )"
insert_skill = "INSERT INTO skill VALUES (?, ?)"

category_list = ["https://wiki.serenesforest.net/index.php/Category:RedCard",
                 "https://wiki.serenesforest.net/index.php/Category:BlueCard",
                 "https://wiki.serenesforest.net/index.php/Category:WhiteCard",
                 "https://wiki.serenesforest.net/index.php/Category:BlackCard",
                 "https://wiki.serenesforest.net/index.php/Category:GreenCard",
                 "https://wiki.serenesforest.net/index.php/Category:PurpleCard",
                 "https://wiki.serenesforest.net/index.php/Category:YellowCard",
                 "https://wiki.serenesforest.net/index.php/Category:BrownCard",
                 "https://wiki.serenesforest.net/index.php/Category:ColorlessCard"]

list_pje = []
