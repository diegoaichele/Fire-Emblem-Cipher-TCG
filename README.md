# Cipher SereneForest

## Resume
In this git I want to show an example of information scrapping, use of SQL language with python and backend with FastAPI.

 - [x] SQLite: Create the database 'cipher_fireemblem.db' with 3 relational table:
    - [x] Table of every card with them information ( name, imageurl, class, cost, etc.). 
    - [x] Table of every skil associated with a card.
    - [x] Table of every affinities associated with a card.
![SQLTAble](repositoryfiles/cipher_sql.png)
 - [x] Scrapper:  Save information of website  https://wiki.serenesforest.net in the SQL table.
    - [x] Visit every hero page. 
    - [x] Debug cards with bad information.
![CardINFO](repositoryfiles/cardinfo.png)

 - [x] FastAPI: Create and API with [FastAPI](https://fastapi.tiangolo.com/)
    - [x] Get endpoint with card all card information 
    
![api404](repositoryfiles/api_not_found.png)
![api200](repositoryfiles/apicardfound.png)



## TODO
 - [ ] Create and TelegramBot and deploy.