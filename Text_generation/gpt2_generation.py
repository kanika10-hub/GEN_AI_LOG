from transformers import pipeline 
import torch

generator = pipeline(
 'text-generation', 
 model='gpt2',
 device=-1  
)

prompt = 'Generative AI will transform education because'
outputs = generator(
 prompt,
 max_new_tokens=100,
 num_return_sequences=3,
 temperature=0.8,  # Randomess / creativity
 do_sample=True,
 top_p=0.95,
 top_k=50
)
for i, output in enumerate(outputs):
 print(f'\n--- Option {i+1} ---')
 print(output['generated_text'])
