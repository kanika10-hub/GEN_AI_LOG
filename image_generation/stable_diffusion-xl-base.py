from huggingface_hub import InferenceClient
import random

client = InferenceClient(
    token="Replace your hf token here"
)

prompt = """
A cinematic futuristic classroom scene,
a highly realistic humanoid AI robot teacher standing at the front of the classroom,
teaching artificial intelligence concepts to university students,
students sitting at modern desks attentively listening,
large holographic AI presentation screen behind the robot,
robot facing the students,
wide-angle professional photography,
cinematic lighting,
depth of field,
ultra realistic,
sharp focus,
highly detailed faces,
modern futuristic interior,
award winning photography,
8k,
masterpiece,
dynamic composition
"""

negative_prompt = """
blurry,
cartoon,
anime,
low quality,
deformed face,
bad anatomy,
extra fingers,
duplicate people,
cropped,
text,
watermark,
floating limbs,
mutated hands,
distorted body,
poor lighting,
empty classroom,
bad perspective
"""

image = client.text_to_image(

    model="stabilityai/stable-diffusion-xl-base-1.0",

    prompt=prompt,

    negative_prompt=negative_prompt,

    width=1024,

    height=1024,

    guidance_scale=9,

    num_inference_steps=40,

    seed=random.randint(1, 100000)
)

image.save("ultimate_ai_classroom.png")
