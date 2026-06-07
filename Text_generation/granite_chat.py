from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = 'ibm-granite/granite-3.1-2b-instruct'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
 model_id,
 torch_dtype=torch.float16,
 device_map='auto'
)

messages = [
 {'role': 'user',
 'content': 'Explain what a transformer is in 3 bullet points for a student.'}
]

input_ids = tokenizer.apply_chat_template(messages, return_tensors='pt')['input_ids'].to(model.device)
output = model.generate(
 input_ids,
 max_new_tokens=256,
 temperature=0.7,
 do_sample=True
)

response = tokenizer.decode(output[0][input_ids.shape[1]:], skip_special_tokens=True)
print(response)
