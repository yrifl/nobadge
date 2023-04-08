import requests, json
from time import sleep
from os import system

uid = int(input("User ID > "))
rbxcookie = str(input("RobloxSecurity Cookie (.ROBLOSECURITY) > "))
system('cls')
print("Initiation.. Deletion")

rif = requests.get(f'https://badges.roblox.com/v1/users/{uid}/badges?limit=100&sortOrder=Asc')

rs = json.loads(rif.text)

ids = []
vedex = []
gameNR = []
gameN = []
cookiesx = {'.ROBLOSECURITY': rbxcookie}
XCSRFTOKEN = requests.post("https://auth.roblox.com/v2/logout", cookies=cookiesx).headers['X-CSRF-TOKEN']
chead = {
    'Content-Type': 'application/json',
    'X-CSRF-TOKEN': XCSRFTOKEN
}

succ = 0
for x in range(len(rs["data"])):
    ids.append(rs["data"][x]["id"])
    vedex.append(rs["data"][x]["name"])
for s in range(len(rs["data"])):
    gameNR.append(rs["data"][s]["awarder"]["id"])

for f in range(len(gameNR)):
    N = requests.get(f"https://games.roblox.com/v1/games/multiget-place-details?placeIds={gameNR[f]}", cookies=cookiesx)
    N = json.loads(N.text)
    gameN.append(N[0]["name"])

def delbd(badgeID):
    global succ
    r = requests.delete(f"https://badges.roblox.com/v1/user/badges/{badgeID}", cookies=cookiesx, headers=chead)
    print(r.text)
    if r.status_code == 200:
        succ += 1

for x in range(len(ids)):
    print(f"[-] Deleting a badge named {vedex[x]} from '{gameN[x]}' game with badge id {ids[x]}")
    delbd(ids[x])

if len(ids) != succ:
    if succ == 0:
        print("[!] Cannot remove any badges :'(. This is a bug maybe...")
    else:
        print(f"[!] Successfuly removed {succ} badges, failed to remove {len(ids)-succ} badges. Sorry!")
else:
    print(f"[+] Successfuly removed {succ} badges, that means all badges removed :D")

print("Thank you for using this software! Created by Cyber2f08. :D")
