import tiktoken
enc = tiktoken.encoding_for_model('gpt-4')
tokens = enc.encode('Generative AI is transforming the world!')
print(f'Tokens: {tokens}') 
print(f'Token count: {len(tokens)}')
print(f'Decoded: {enc.decode(tokens)}')

