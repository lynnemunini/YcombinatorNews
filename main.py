from bs4 import BeautifulSoup
import requests
import os
from twilio.rest import Client
import lxml
account_sid = os.environ["AUTH_SID"]
auth_token = os.environ["AUTH_TOKEN"]
# with open("website.html", mode="r") as my_data:
#     data = my_data.read()
#
# soup = BeautifulSoup(data, 'lxml')
# # To indent the html file
# # print(soup.prettify())
# # title = soup.title
# # print(title.name)
# # print(title.string)
# # print(soup.a)
# # all_a = soup.findAll(name="a")
# # print(all_a)
# # for each in all_a:
# #     # print(each.getText())
# #     # get the links
# #     print(each.get("href"))
#
# # all_h1 = soup.find(name="h1", id="name")
# # print(all_h1.getText())
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
# heading = soup.select(".heading")
# print(heading[0])

# Scraping a live website
response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "lxml")
anchors = soup.findAll(name="a", class_="titlelink")
upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
anchor_text_list = []
anchor_link_list = []
# print(upvotes)
num = 1
my_val = 0
for each in anchors:
    anchor_text = each.getText()
    anchor_text_list.append(anchor_text)
    anchor_link = each.get("href")
    anchor_link_list.append(anchor_link)
    # print(f"{num}. {anchor_text}")
    # print(f"\t {anchor_link}")
    num += 1
# print(anchor_text_list)
# print(anchor_link_list)
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
    body=f"🗞Top latest news from https://news.ycombinator.com\n\n"
         f"{anchor_text_list[0]}\n{anchor_link_list[0]}\n\n{anchor_text_list[1]}\n{anchor_link_list[1]}\n\n"
         f"{anchor_text_list[2]}\n{anchor_link_list[2]}\n\n",
    from_='+18454980776',
    to=os.environ["NUMBER"]
        )
print(message.status)
