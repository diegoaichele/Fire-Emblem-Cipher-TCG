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
for category in category_list:
    r = requests.get( category )
    soup = BeautifulSoup(r.content, 'html.parser')
    list_link_personaje = [personaje.a["href"] for personaje in soup.find(attrs ={"class":"mw-content-ltr"}).find_all("li")]
    print(category)
    time.sleep(1.2)

    for pje in list_link_personaje:
        if pje in list_pje:
            continue
        else:
            list_pje.append( pje )
            
        r = requests.get("https://wiki.serenesforest.net" + pje )
        time.sleep(1.3)
        soup = BeautifulSoup(r.content, 'html.parser')

        page_pje = soup.find_all("table", attrs ={"class":"sf"} )

      

        for index in range(len(page_pje) ):
            card_name =  page_pje[index].th.text
            try:
                card_image_url = page_pje[index].find_all("td")[0].img["srcset"].split(" ")[0]
            except:
                card_image_url = page_pje[index].find_all("td")[0].img["src"]
            card_class = page_pje[index].find_all("td")[2].text
            card_cost = page_pje[index].find_all("td")[4].text
            card_symbol1 = page_pje[index].find_all("td")[6].find_all("img")[0]["alt"]
            card_symbol2 = page_pje[index].find_all("td")[6].find_all("img")[1]["alt"]
            card_list_affinities = [affinities["alt"] for affinities in page_pje[index].find_all("td")[8].find_all("img") if affinities["alt"] != "None"]

            card_attack = page_pje[index].find_all("td")[10].text
            card_support = page_pje[index].find_all("td")[12].text
            card_range = page_pje[index].find_all("td")[14].text

            card_quote = page_pje[index].find_all("td")[16].text

            list_index_skill = [skill_index+1 for skill_index, skill_value in enumerate(page_pje[index].find_all("td")) if "Skill" in str(skill_value.text)]
            list_index_skill = [n for n in list_index_skill if n%2 == 0]
            list_skill = []
            for index_skill in list_index_skill:  
                the_skill = page_pje[index].find_all("td")[index_skill].text
                for alt in [img["alt"] for img in  page_pje[index].find_all("td")[index_skill].find_all("img")]:
                    alt = alt.upper()
                    the_skill = the_skill.replace("  "," |"+alt+"| ",1)
                list_skill.append(the_skill)
            list_skill

            card_code = page_pje[index].find_all("td")[-5].text
            card_illustrator = page_pje[index].find_all("td")[-3].text
            card_comment = page_pje[index].find_all("td")[-1].text

            list_card_code = card_code.split(" / ")
            for the_card_code in list_card_code:
                  
                no_pass = False
                    
                for row in cur.execute(" Select * from card where ID=:ID", {"ID": the_card_code}):
                    if row[0] == the_card_code:
                        the_card_code += "signed"
                        print(the_card_code,"  -   " ,card_name)
                     
                    
                for row in cur.execute(" Select * from card where ID=:ID", {"ID": the_card_code}):
                    if row[0] == the_card_code:
                        no_pass = True
                        
                if no_pass:
                    print(the_card_code,"  -   " ,card_name)
                    continue

                download_img(card_image_url, the_card_code )
                # Insert Card
                cur.execute( insert_card, ( the_card_code , card_name, card_image_url, card_class, card_cost,
                                        card_symbol1, card_symbol2, card_attack, card_support, card_range,
                                        card_quote, card_illustrator, card_comment))

                #  Insert Skill
                for the_skill in list_skill:
                    cur.execute( insert_skill, (the_card_code,the_skill) )
                
                # Insert affinities
                for the_affinities in card_list_affinities:
                    cur.execute( insert_affinities, (the_card_code,the_affinities) )

            con.commit()