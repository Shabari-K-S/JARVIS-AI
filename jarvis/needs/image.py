from diffusers import DiffusionPipeline
import os

def prompt_image(prompt, obj):
    pipe = DiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
    pipe = pipe.to("cpu")

    image = pipe(prompt).images[0]
    # get the count of files in the directory
    # and increment the count by 1 to get the next file name
    count = len(os.listdir("generated_image"))

    image.save(f"generated_image/{count+1}.png")
    obj.update_inage()

if __name__ == "__main__":
    prompt_image("Astronaut in a jungle, cold color palette, muted colors, detailed, 8k")