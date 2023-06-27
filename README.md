# ~~Carter-CeV1-WebSocket~~ NOT WORKING ANYMORE
This is a simple Python implementation of the Carter API, which uses WebSockets for real-time communication. It provides a basic integration that can be used as a starting point for building more advanced applications. The code includes a `send_message()` function that sends a message to the API and waits for a response before returning it. The response is then printed to the console. Additionally, the code handles disconnections from the API and attempts to reconnect automatically when a new message is sent. Note that this is a basic implementation and may require further customization for your specific use case.

## Before usage
You have to change two variables in the script.
```python
API_KEY = 'YOUR_API_KEY'
PLAYER = 'YOUR_CUSTOM_ID_FOR_EACH_USER'
URL = "https://dev-api.carterapi.com"
```
URL have to stay the same!!!

## Usage/Example

```python
from CarterSocket import send_message

while True:
    message = input('Your message: ')
    response_data = send_message(message)
    print(f"Response: ", response_data["output"]["text"])
```

# Made with: 
<a href="https://www.carterapi.com"><img src="https://charles.mislead.dev/icons/carterapi.png" style="width: 200px;" /></a>
<a href="https://www.python.org/"><img src="https://charles.mislead.dev/icons/MadeWithPython.png" style="width: 200px;" /></a>
