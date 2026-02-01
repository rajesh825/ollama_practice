import ollama


# Example1
# response = ollama.list()
# print(response)

# Example 2 - Using Ollam Chat api
# res = ollama.chat(
#     model="llama3.2",
#     messages=[{"role": "user", "content": "Tell me short story and make it funny"}],
# )

# print(res["message"]["content"])

# Example 3 - Using Ollama Chat api with different parameters
# Specifying stream as True
res = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": "Tell me short story and make it funny"}],
    stream=True,
)

# Iterating over the streamed response
for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)

# Example 4 - Using Ollama Generate api

res = ollama.generate(model="llama3.2", prompt="Why is the sky blue ?")

# Show the generated text
# print(ollama.show("llama3.2"))
print(res["response"])
