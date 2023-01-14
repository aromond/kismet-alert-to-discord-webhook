from discord_webhook import DiscordWebhook
import websocket
import _thread
import time
import rel
import json

discord_webhook_url = "DISCORD_WEBHOOK_URL"
kismet_server = "HOSTNAME_FOR_KISMET_SERVER"
kismet_api_key = "KISMET_API_KEY" 

def on_message(ws, message):
    webhook = DiscordWebhook(url=discord_webhook_url, rate_limit_retry=True, content=message)
    response = webhook.execute()
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")
    json = '{ "SUBSCRIBE": "ALERT" }'
    ws.send(json)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://" + kismet_server + ":2501/eventbus/events.ws?KISMET=" + kismet_api_key ,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
