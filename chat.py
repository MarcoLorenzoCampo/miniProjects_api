import openai
import os

def main():
    openai.api_key = get_key()
    gpt_comm()

def gpt_comm():
    messages = []
    sys_msg = "Opening chat, end it with <quit()>?\n"
    print(sys_msg)
    messages.append({"role":"system", "content":sys_msg})
    messages.append({"role":"user", "content":"Hello"})

    while input != 'quit()':
        message = input()
        messages.append({"role":"user", "content":message})

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