#try it yourself
txtmessages = ['xoxo', 'hey!', 'ttyl']
def show_messages(txtmessages):
    for txt in txtmessages:
        print(txt)

show_messages(txtmessages)

def send_messages(txtmessages, sent_messages):
    while txtmessages:
        txt = txtmessages.pop()
        print(f"\nSending:{txt}")
        sent_messages.append(txt)

def show_sent(sent_messages):
    print("\nMessage Received")
    for sent_txt in sent_messages:
        print(sent_txt)

sent_messages=[]

send_messages(txtmessages[:],sent_messages)
show_sent(sent_messages)

print(txtmessages)