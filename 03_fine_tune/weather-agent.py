from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

# Initialize Gemini
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Tools
def get_weather(city: str):
    print("🔨 Tool Called: get_weather", city)
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text.strip()}."
    return "Something went wrong"

def run_command(command):
    print("🔨 Tool Called: run_command", command)
    return os.popen(command).read()

# Tool registry
available_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes a city name as an input and returns the current weather for the city"
    },
    "run_command": {
        "fn": run_command,
        "description": "Takes a command as input to execute on system and returns output"
    }
}

# System Prompt
system_prompt = """
You are an helpful AI Assistant who is specialized in resolving user queries.
You work in start → plan → action → observe → output mode.
Given a user query and available tools, plan the steps, call the relevant tool,
observe the result, and finally resolve the query.

Rules:
- Output in JSON format strictly.
- Perform one step at a time, wait for the next input.
- Carefully analyze each step.

Output Format:
{
    "step": "string",
    "content": "string",
    "function": "string",
    "input": "string"
}

Available Tools:
- get_weather: Takes a city name as input and returns the weather.
- run_command: Takes a shell command as input and returns the output.

Example:
User Query: What is the weather in New York?
Output: {"step": "plan", "content": "The user wants weather info for New York."}
Output: {"step": "plan", "content": "I'll use get_weather tool."}
Output: {"step": "action", "function": "get_weather", "input": "New York"}
Output: {"step": "observe", "content": "It's sunny in New York, 25°C"}
Output: {"step": "output", "content": "The weather in New York is sunny and 25°C."}
"""

# Create chat
chat = client.chats.create(
    model="gemini-2.0-flash-lite",
    config={
        "system_instruction": system_prompt,
        "temperature": 0.7,
        "response_mime_type": 'application/json',
    }
)

# Start conversation

while True:
    query = input(">>> ")
    step_input = query

    while True:
        response = chat.send_message(step_input)
        if response.text is None:
            raise ValueError("Empty response!")

        output = json.loads(response.text)
        step = output.get("step")
        content = output.get("content")

        if step == "plan":
            print("🧠", content)
            step_input = "next"  # just prompt next step
            continue

        elif step == "action":
            tool_name = output.get("function")
            tool_input = output.get("input")

            if tool_name in available_tools:
                tool_fn = available_tools[tool_name]["fn"]
                result = tool_fn(tool_input)
                step_input = json.dumps({
                    "step": "observe",
                    "content": result
                })
            else:
                print("❌ Tool not found:", tool_name)
                break

        elif step == "observe":
            print("🔎", content)
            step_input = "next"
            continue

        elif step == "output":
            print("✅", content)
            break

        else:
            print("⚠️ Unknown step:", step)
            break
