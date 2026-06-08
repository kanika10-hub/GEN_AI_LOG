from transformers import pipeline
classifier = pipeline('sentiment-analysis')
texts = [
 'Generative AI is revolutionizing every industry!',
 'AI systems are biased and dangerous.',
 'I am neutral about AI developments.'
]
results = classifier(texts)
for text, result in zip(texts, results):
 print(f'{result["label"]:10} ({result["score"]:.3f}) | {text[:60]}')


# Generator
generator = pipeline('text-generation', model='gpt2')
prompt = 'The future of generative AI in education is'
generated = generator(prompt, max_new_tokens=60, do_sample=True, temperature=0.9)
print(f'\nGenerated text:\n{generated[0]["generated_text"]}')
