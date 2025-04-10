from  openai import OpenAI

load_dotenv()

client = OpenAI()

text = "Avengers is og movie"

response = client.completions.create(
    prompt=text,
    model='text-davinci-003'
)

print('response => ', response.choices[0].text)