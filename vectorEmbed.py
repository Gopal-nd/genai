from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "Avengers is og movie"

response = client.embeddings.create(
    input=text,
    model='text-embedding-3-small'
)


print('vecor embedings => ', response.data[0].embedding)