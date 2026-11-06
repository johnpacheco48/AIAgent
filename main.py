import argparse
import json
import os
import sys

from dotenv import load_dotenv

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if os.environ.get("OPENROUTER_API_KEY") == None: raise RuntimeError("API_Key no worki")

    from openai import OpenAI

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Input prompt for Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()




    messages: list[dict[str, str]]=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    for _ in range(20):
        if _ >= 20:
           print(f"Error: failed to return result after {_} tries")
           sys.exit(1)
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )
        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message)
                if result_message["content"] is None: raise Exception(f"Error: No result message content")
                if args.verbose is True:
                    print(f"-> {result_message['content']}")
                else:
                    print(result_message['content'])
        if response.usage == None: raise RuntimeError("No response generated")
        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}")
        if message.tool_calls is None:
            print(f"Response:\n{response.choices[0].message.content}")




main()
