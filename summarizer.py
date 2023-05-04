import openai
import os

def main():
    openai.api_key = get_key()
    gpt_comm()

def gpt_comm():

    with open("paper.txt", "r", encoding='utf-8') as paper:
        content = paper.read()

        messages = []
        sys_msg = "Reading from paper... Done. What do you want to know?\n"
        messages.append({"role":"system", "content":sys_msg})
        messages.append({"role":"user", "content":content + '\nsummarize it with 50 words'})

        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages=messages,
                temperature=0.1
            )

        reply = response["choices"][0]['message']['content']
        messages.append({"role":"assistant", "content":reply})

        print("\n"+reply+"\n")
    
    return

def get_key():
    key = os.environ.get("OPENAI_API_KEY")
    return key

main()