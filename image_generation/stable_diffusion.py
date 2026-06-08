from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
 'runwayml/stable-diffusion-v1-5',
 torch_dtype=torch.float16
)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
pipe = pipe.to(device)

prompt = '''A photorealistic image of a robot teaching AI to students in a classroom,
dramatic lighting, 8k'''
negative_prompt = 'blurry, cartoon, low quality, watermark, text'
image = pipe(
 prompt=prompt,
 negative_prompt=negative_prompt,
 num_inference_steps=50,
 guidance_scale=7.5,
 width=512,
 height=512,
 generator=torch.manual_seed(42)

).images[0]
image.save('ai_classroom.png')
print('Image generated and saved!')

