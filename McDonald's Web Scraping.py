import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.mcdonalds.co.id/menu#Sarapan%20Pagi"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

cards = soup.find_all("a", class_="card-menu")

with open("mcd_menu.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["product_name", "product_link", "image_url", "category"])

    for card in cards:
        name = card.find("p").get_text(strip=True)
        link = card.get("href")
        img = card.find("img").get("src")

        writer.writerow([name, link, img, "Sarapan Pagi"])

print("CSV berhasil dibuat!")

