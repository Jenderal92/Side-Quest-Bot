import requests

ID = "1732587701436xxxxx"
PASTE_BEARER = "Bearer 1732587701436870656-xxxxxxxxxx"
API_URL = 'https://lb.backend-sidequest.rcade.game/users/' + ID

headers = {
    'Authorization': PASTE_BEARER,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

def get_user_data(session, url, headers):
    response = session.get(url, headers=headers)
    return response.json()

def bypass_missions(session, user_data, url, headers):
    for mission in user_data['availableQuests']:
        print("Try Bypass  =>> " + mission['title'])
        mission_id = mission['_id']
        complete_url = url + "/quests/" + str(mission_id)
        response = session.post(complete_url, headers=headers)
        print("[Done Bypass]  =>> " + mission['title'])
        print("[Done Bypass]  =>> " + str(mission['type']))
        print("[You Get Points]  =>> " + str(mission['points']))

session = requests.Session()
user_data = get_user_data(session, API_URL, headers)

if 'user' in user_data:
    print("Side Quest Auto Complete Task")
    print("Success Log In  =>> " + user_data['user']['twitterHandle'])
    print("Process Bypass Follow .....")
    bypass_missions(session, user_data, API_URL, headers)
