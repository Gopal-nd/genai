from dotenv import load_dotenv
# from google import genai 
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY_IS")

print(api_key)

# prompt = """
# you are the ai assianetent ai assisnt who is expert in the resolning the user query ,
 
# """

# client = genai.Client(api_key=api_key)

# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="give me the current wether of he anekal in one line"
# )
# print(response.text)