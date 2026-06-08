from huggingface_hub import InferenceClient
client = InferenceClient(token=' Replace you token here ')

#the client acts as a bridge to communicate with remote infrastructure

print('\n--- Image Generation (via InferenceClient) ---')
try:
  image = client.text_to_image(
      model="stabilityai/stable-diffusion-xl-base-1.0",
      prompt='A photorealistic robot teaching students infront a classroom'
  )
 
  if image:
    image.save('generated_image_client.jpg')
    print('Image saved as generated_image_client.jpg!')
  else:
    print('Image generation returned no image.')
except Exception as e:
  print(f"Error during image generation with InferenceClient: {e}")






