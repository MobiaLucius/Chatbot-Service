import openai
import os
import logging as log

log.basicConfig(filename='history.log', encoding='utf-8', level=log.DEBUG)

openai.api_key = os.environ.get("OPENAI_API_KEY") #change to your api key to use
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    user_input = input("You: ")
    if user_input == 'exit':
        break
    
    log.info('Q:' + user_input)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    log.info(response)
    
    print('Chatbot: '+str(response['choices'][0]['message']['content'])+'\n')
    messages.append(response['choices'][0]['message'])