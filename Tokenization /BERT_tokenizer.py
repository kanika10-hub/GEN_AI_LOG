
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
encoded = tokenizer('Hello, I am learning about LLMs!', return_tensors='pt')
print('Input IDs:', encoded['input_ids'])
print('Tokens:', tokenizer.convert_ids_to_tokens(encoded['input_ids'][0]))

