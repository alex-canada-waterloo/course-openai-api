"""
https://platform.openai.com/docs/guides/text-generation?lang=python
Roles:
    User - a request to generate the output
    System - top level instructions to the model
    Assistant - multi-turn conversation
"""

from openai import OpenAI
client = OpenAI()

# Create a human-like response to a prompt
generateProseResponse = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)
print(generateProseResponse.choices[0].message)

# Generate JSON
generateJson = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "you extract email addresses into JSON data as array"
        },
        {
            "role": "user",
            "content": "Felling stuck? Send a message to help@mycompany.com."
        },
        {
            "role": "user",
            "content": "For pricing inquries please contact sales@mycompany.com."
        }
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "email_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "email": {
                        "description": "The email address that appears in the input",
                        "type": "string"
                    },
                    "additionalProperties": False
                }
            }
        }
    }
)
print(generateJson.choices[0].message.content)


