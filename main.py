import requests
import json



data_dic= {}
with open("data.json", "r") as f:
    data_dic = json.load(f)


NOTION_TOKEN = data_dic["notion_token"]
DATABASE_ID = data_dic["data_id"]

headers = {
        'Authorization': f'Bearer {NOTION_TOKEN}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json'
        }

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"
    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}
    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    print("Response Body:", res.json())
    return res


def read_database():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for result in data["results"]:
            print(result["properties"]) 
    else:
        print(f"Error: {response.status_code}", response.text)


title = data_dic["title"]
chanal_id = "@Notion_link_store_bot"
user_id = str(data_dic["user_id"])
user_name = data_dic["user_name"]
link = data_dic["link"]
data = {
    "URL": {"title": [{"text": {"content": link}}]},
    "Title": {"rich_text": [{"text": {"content": title}}]},
    "id канала": {"rich_text": [{"text": {"content": chanal_id}}]},
    "id_пользователя": {"rich_text": [{"text": {"content": user_id}}]},
    "User_Name": {"rich_text": [{"text": {"content": user_name}}]}
}
create_page(data)
