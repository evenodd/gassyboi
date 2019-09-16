import sys
import time
from pprint import pprint
from dialect import Dialect
from sensor import Sensor
from state_alerter import StateAlerter
from notifier import Notifier

lame_gassy_boi = True

webhook_url = "https://hooks.slack.com/services/ADD_YOUR_SLACK_WEBHOOK_HERE"
webhook_headers = {"Content-type" : "application/json"}

notifier = Notifier(
    Dialect("lame" if lame_gassy_boi else "cool"),
    webhook_url
)

if (len(sys.argv) > 1):
    sensor = Sensor(notifier.send_disconnect_notification, notifier.send_reconnect_notification, url=sys.argv[1])
else:
    sensor = Sensor(notifier.send_disconnect_notification, notifier.send_reconnect_notification)


co2State = StateAlerter(
    {
        "safe" :        0,
        "risky" :       1000,
        "serious" :     2000,
        "dangerous" :   5000,
        "fatal" :       40000
    },
    "safe",
    notifier.send_co2_up_notification,
    notifier.send_co2_down_notification
)

vocState = StateAlerter(
    {
        "safe" :      0,
        "risky" :     560,
        "dangerous" : 1150
    },
    "safe",
    notifier.send_voc_up_notification,
    notifier.send_voc_down_notification
)

while True:
    time.sleep(1)
    co2, voc = sensor.sample()
    co2State.update(co2)
    vocState.update(voc)
