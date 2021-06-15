import vk_api
import random
token = TOKEN


vk = vk_api.VkApi(token=token)

vk._auth_token()
#OPENING FILES
fs = open("Senior_C2.txt", encoding="UTF-8").read().split("\\n\n")

for i in range(len(fs)):
    num = int(str(fs[i][:3:]))
    fs[i]= [num, fs[i][3::]]

fj = open("Junior_C2.txt", encoding="UTF-8").read().split("\\n\n")

for i in range(len(fj)):
    num = int(str(fj[i][:2:]))
    fj[i] = [num, fj[i][2::]]
    
#DEFS
def seniorC2(x):
    global fs
    a = []
    for i in range(x):
        if not(fs[random.randint(0, len(fs)-1)] in a):
            a.append(fs[random.randint(0, len(fs)-1)])
    a = sorted(a)
    for i in range(len(a)):
        a[i] = str(a[i][0])+" "+str(a[i][1])
    a = "\n".join(a)
    return a

def juniorC2(x):
    global fj
    a = []
    for i in range(x):
        a.append(fj[random.randint(0, len(fj)-1)])
    a = sorted(a)
    for i in range(len(a)):
        a[i] = str(a[i][0])+" "+str(a[i][1])
    a = "\n".join(a)
    return a

def sender(id, my_message):
    vk.method("messages.send", {"peer_id": id, "message": my_message, "random_id": random.randint(1, 2147483647)})


while True:

        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            user_id = messages["items"][0]["last_message"]["from_id"]
            user_msg = messages["items"][0]["last_message"]["text"]
            user_msg = user_msg.lower()
            user_msg_list = user_msg.split()
            if user_msg == "команды":
                sender(user_id, "Список команд:\n\n"
                       "/juniorc2 <Количество треков> - команда для создания трек листа для junior в cytus2\n\n"
                       "/seniorc2 <Количество треков> - команда для создания трек листа для senior в cytus2\n"
                       )
            elif user_msg_list[0] == "/juniorc2":
                try:
                    sender(user_id, juniorC2(int(user_msg_list[1])))
                except Exception:
                    sender(user_id, "После команды введите целое число")

            elif user_msg_list[0] == "/seniorc2":
                try:
                    sender(user_id, seniorC2(int(user_msg_list[1])))
                except Exception:
                    sender(user_id, "После команды введите целое число")






