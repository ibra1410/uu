import telepot
from telepot.loop import MessageLoop
import google.generativeai as genai
genai.configure(api_key="AIzaSyAilAGJig7Z7Jw0ttO0mXZEEVxVQoFWsnY")
model = genai.GenerativeModel('gemini-pro')

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']
    response = model.generate_content(text)
    telepot.bot.sendMessage(chat_id, response.text)

telepot.bot = telepot.Bot('7408633253:AAFO8nD7XrVqa2L-XMzJoXpZ7XnVoQEy1fA')
MessageLoop(telepot.bot, handle).run_forever()
print('Listening ...')
