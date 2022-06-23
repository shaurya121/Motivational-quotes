import requests
url='https://api.adviceslip.com/advice'
def fun():
    data=requests.get(url)
    json_data=data.json()
    ran_advice=json_data['slip']
    print(ran_advice['advice'])

fun()
