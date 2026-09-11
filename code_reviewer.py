import os
from openai import OpenAI

client = OpenAI(
    api_key="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", 
    base_url="https://openrouter.ai/api/v1"
)

with open("REVIEW.md", "w", encoding="utf-8") as review_file:
    review_file.write("# Automated Code Review Report\n\n")
    
    for file in os.listdir("."):
        if file.endswith((".py", ".java", ".cpp")):
            print(f"Reviewing {file}...")
            with open(file, "r", encoding="utf-8") as f:
                code = f.read()
            
            response = client.chat.completions.create(
                model="openrouter/free",
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": f"Review this code for bugs, efficiency issues, and best practices. Provide structured feedback:\n\n{code}"}
                ]
            )
            
            feedback = response.choices[0].message.content
            review_file.write(f"## File: {file}\n{feedback}\n\n---\n\n")

print("Code review complete. Check REVIEW.md for results.")