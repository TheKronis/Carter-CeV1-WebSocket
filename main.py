import socketio

API_KEY = 'YOUR_API_KEY'
PLAYER = 'YOUR_CUSTOM_ID_FOR_EACH_USER'
URL = "https://dev-api.carterapi.com"

sio = socketio.Client()

response_queue = []

@sio.event
def connect():
    print('Connected to Carter API server')

@sio.event
def message(data):
    response_queue.append(data)

@sio.event
def hash(data):
    global ACCESS_TOKEN
    ACCESS_TOKEN = data
    print('Received access token:', ACCESS_TOKEN)


def send_message(message):
    response_queue.clear()
    sio.emit('message', {'text': message, 'hash': ACCESS_TOKEN})
    while not response_queue:
        pass
    return response_queue.pop()

sio.connect(URL, headers={'key': API_KEY, 'player': PLAYER}, wait_timeout=10)

while True:
    message = input('Your message: ')
    response_data = send_message(message)
    print(f"Response: ", response_data["output"]["text"])
