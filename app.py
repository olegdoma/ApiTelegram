import requests

API_link = "https://api.telegram.org/bot1160757277:AAE36oz6GgBEOSbCjSHnZ08gg3ECV5egZM4"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()
# for keys, values in updates.items():
#     print("keys = ", keys)
#     print("values = ", values)

message = updates["result"][0]["message"]
chat_id = message["chat"]["id"]
text = message["text"]

send_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text= Привет, ты написал {text}")

