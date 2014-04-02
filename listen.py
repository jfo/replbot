import zulip
import sys

replbot = zulip.Client(email="replbot-bot@students.hackerschool.com",
                      api_key="qbEoB8zXKK2Z3CKPTHgkstC1txsT2ooI")

replbot.call_on_each_message(lambda msg: sys.stdout.write(str(msg) + "\n"))

# replbot.send_message({
#     "type": "private",
#     "to": "jeffowler@gmail.com",
#     "content": "I have a voice, and yet no ear!"
# })
