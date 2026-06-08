'''installation of transformers 
diffusers and upgrade hg'''
!pip install transformers datasets accelerate
!pip install diffusers
!pip install --upgrade huggingface_hub

from huggingface_hub import login
login(token=' Replace your token here ')


from huggingface_hub import HfApi, list_models
api = HfApi()

models = list(
    list_models(
        filter='text-generation',
        sort='downloads',
        limit=5
    )
)
print('Top 5 Text Generation Models:')
for m in models:
    print(f' {m.modelId} — {m.downloads:,} downloads')


model_info = api.model_info('ibm-granite/granite-3.1-2b-instruct')
print('\nModel Tags:', model_info.tags)


