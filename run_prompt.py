"""
run_prompt.py
-------------
Test any prompt from this library against the Anthropic API.

SETUP (one time only):
    pip install anthropic
    export ANTHROPIC_API_KEY="your-key-here"

USAGE:
    1. Copy a prompt template from the /prompts folder
    2. Fill in the [VARIABLES] with your actual content
    3. Paste the filled prompt into the PROMPT variable below
    4. Run: python run_prompt.py
"""

import anthropic
import os

# PASTE YOUR FILLED PROMPT HERE

PROMPT = """
Replace this text with your filled prompt template.
Copy from any file in the /prompts folder.
Fill in all [VARIABLES] before running.
"""

# OPTIONAL: ADD A SYSTEM PROMPT
# Leave as None if you do not need one.

SYSTEM_PROMPT = None

# DO NOT EDIT BELOW THIS LINE

def run(prompt, system_prompt=None):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "\n\nANTHROPIC_API_KEY not found.\n"
            "Set it by running this in your terminal first:\n"
            "    export ANTHROPIC_API_KEY='your-key-here'\n"
        )

    client = anthropic.Anthropic(api_key=api_key)

    kwargs = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}],
    }

    if system_prompt:
        kwargs["system"] = system_prompt

    message = client.messages.create(**kwargs)
    return message.content[0].text


if __name__ == "__main__":
    print("\n── Running prompt ──────────────────────────\n")
    result = run(PROMPT, SYSTEM_PROMPT)
    print(result)
    print("\n── End of output ───────────────────────────\n")
