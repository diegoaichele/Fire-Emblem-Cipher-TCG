from fastapi import FastAPI, HTTPException
import sqlite3


app = FastAPI()

         
con = sqlite3.connect('cipher_fireemblem.db' , check_same_thread=False)
cur = con.cursor()

app = FastAPI()


@app.get("/")
def read_root():
    return {"staus": "ok"}


@app.get("/card_id/{card_id}")
def read_item(card_id: str):
    """Retrieve a card by id

    Args:
        card_id (str): card id from firemblem card database.

    Returns:
        dict/json: All information of card
    """
    select_card = "SELECT * FROM card WHERE ID = (?)"
    select_skill = "SELECT * FROM skill WHERE ID = (?)"
    select_affinities = "SELECT * FROM affinities WHERE ID = (?)"
    column_name =  ["ID", "name", "imageurl", "class", "cost", "symbol1", "symbol2", "attack", "suppport", "range", "quote", "illustrator", "comment"]
    card = cur.execute(select_card, (card_id,) )
    index = 0
    for index,value in enumerate(card):
        card_dict = {column_name[index_value]:infomation_value for index_value,infomation_value in enumerate(value)}
        index += 1
        break
    if index == 0:
        raise HTTPException(status_code=404, detail="Card not found")
    skills = cur.execute(select_skill, (card_id,) )
    card_dict["skills"] = [i[1] for i in skills]
    affinities = cur.execute(select_affinities, (card_id,) )
    card_dict["affinities"] = [i[1] for i in affinities]
    card_dict["status"] = "200"
    return card_dict