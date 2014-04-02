import zulip
import sys

replbot = zulip.Client(email="replbot-bot@students.hackerschool.com",
                      api_key="qbEoB8zXKK2Z3CKPTHgkstC1txsT2ooI")

# replbot.call_on_each_message(lambda msg: sys.stdout.write(str(msg) + "\n"))

replbot.send_message({
    "type": "private",
    "to": "robsoko315@gmail.com",
    "content": "so i guess it is as simple as having a running instance of your script somewhere... since its not using a restful http thing... you dont have to set up any server handling"
})
