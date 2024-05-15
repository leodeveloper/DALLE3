from openai import OpenAI

client = OpenAI(api_key="")

response = client.images.generate(
  model="dall-e-3",
  prompt="write a biryani receipe in urdu",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)