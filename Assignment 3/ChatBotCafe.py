#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define the states
INIT=0 
CHOOSE_COFFEE=1
ORDERED=2

# Define the policy rules dictionary
policy_rules = {
    (INIT, "ask_explanation"): (INIT, "I'm a bot to help you order coffee beans"),
    (INIT, "order"): (CHOOSE_COFFEE, "ok, Colombian or Kenyan?"),
    (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "perfect, the beans are on their way!"),
    (CHOOSE_COFFEE, "ask_explanation"): (CHOOSE_COFFEE, "We have two kinds of coffee beans - the Kenyan ones make a slightly sweeter coffee, and cost $6. The Brazilian beans make a nutty coffee and cost $5.")    
}


def interpret(message):
    msg = message.lower()
    if 'order' in msg:
        return 'order'
    if 'kenyan' in msg or 'colombian' in msg:
        return 'specify_coffee'
    if 'what' in msg:
        return 'ask_explanation'
    return 'none'

def respond(state, message):
    (new_state, response) = policy_rules[(state, interpret(message))]
    return new_state, response


def send_message(state, message):
    #print("USER : {}".format(message))
    new_state, response = respond(state, message)
    print("BOT : {}".format(response))
    return new_state


# Define send_messages()
# def send_messages(messages):
#     state = INIT
#     for msg in messages:
#         state = send_message(state,msg)


# send_messages([
#     "what can you do for me?",
#     "well then I'd like to order some coffee",
#     "what do you mean by that?",
#     "kenyan"
# ])




print("""
try these following  questions
what can you do for me?
well then I'd like to order some coffee
what do you mean by that?
kenyan
bye
""")

n = 0
con=True
state = INIT
while con==True:
    user = input()
    if user=='bye':
        print("Please wait don't go sir")
        break
    state = send_message(state,user)
    
    


# In[ ]:




