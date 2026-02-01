import ollama

# Create a new model with model file
modelfile = """
FROM llama3.2
SYSTEM '''
You are very smart assistant who know everything about AI, Finance, Oceans. You are very informative and precise.
'''
PARAMETER temperature 0.1

"""

ollama.create(
    model="knowitall", modelfile=Modelfile
)

res = ollama.generate(model="knowitall", prompt="Why the ocean is so salty.")

print(res["response"])
