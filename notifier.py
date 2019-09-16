import requests
from dialect import Dialect
from state_alerter import StateAlerter

class Notifier:
    
    webhook_headers = {"Content-type" : "application/json"}
    
    def __init__(self, dialect : Dialect, webhook_url):
        self.dialect = dialect
        self.webhook_url = webhook_url

    def _sendSlackMsg(self, msg : str):
        print("Sending message '%s'" % msg)
        resp = requests.post(
            self.webhook_url,
            data = "{\"text\" : \"%s\"}" % msg,
            headers=self.webhook_headers
        )

    def send_disconnect_notification(self) :
        self._sendSlackMsg(self.dialect.get_disconnect())

    def send_reconnect_notification(self) :
        self._sendSlackMsg(self.dialect.get_connect())

    def send_co2_up_notification(self, state : StateAlerter, value):
        self._sendSlackMsg(self.dialect.get_co2_up(state.curr_state, state.get_curr_state_value(), value))

    def send_co2_down_notification(self, state : StateAlerter, value):
        self._sendSlackMsg(self.dialect.get_co2_down(state.last_state, state.curr_state, value))

    def send_voc_up_notification(self, state : StateAlerter, value):
        self._sendSlackMsg(self.dialect.get_voc_up(state.curr_state, state.get_curr_state_value(), value))

    def send_voc_down_notification(self, state : StateAlerter, value):
        self._sendSlackMsg(self.dialect.get_voc_down(state.last_state, state.curr_state, value))

