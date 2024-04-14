from openai import OpenAI
import os
import json
import time


client = OpenAI(
    # This is the default and can be omitted
  
)
    

# def queryGPT(prompt, content):
def getTopic(message):
    print("running gpt3.5 query")
    # message = f"""{prompt}\n\n{content}"""
    # input(message)
    messageArray =[
                {"role": "system", "content": f"You are an expert at taking a question, and returning the best search term to find the answer on wikipedia. Must be no longer than 3 words"},
            ]
    
    
    messageArray.append({"role": "user", "content":f"What is the topic of this question?\n\n {message}"})

    # print(messageArray)

    chat_completion = client.chat.completions.create( model="gpt-3.5-turbo",
    # response = openai.ChatCompletion.create( model="gpt-4",
        messages=messageArray,
        max_tokens=30,
        n=1,
        stop=None,
        temperature=0.1,

    )
    
    message = chat_completion.choices[0].message.content
    return message


def queryGPT(message):
    print("running gpt3.5 query")
    # message = f"""{prompt}\n\n{content}"""
    # input(message)
    messageArray =[
                {"role": "system", "content": f"You are an expert research assistent. You take a question, and a document. You answer any question you are given by refering to the information in the document. Provide a reference."},
            ]
    
    
    messageArray.append({"role": "user", "content":message})

    # print(messageArray)

    chat_completion = client.chat.completions.create( model="gpt-4-turbo-preview",
    # response = openai.ChatCompletion.create( model="gpt-4",
        messages=messageArray,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.1,

    )
    
    message = chat_completion.choices[0].message.content
    return message



