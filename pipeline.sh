echo "Running pipeline"
echo "Creating Database"
python create_database.py
sleep 3
echo "Running Scraper"
python scrapping_card.py