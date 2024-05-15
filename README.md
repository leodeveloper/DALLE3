# DALLE3 Image generation
Image generation with DALL·E 3, dall-e-3

# Image Generations API

The Image Generations API allows you to create original images based on text prompts. It utilizes the DALL·E model, which can generate images of varying sizes.

## Usage

### Endpoint

```http
POST /generate-image

Generations
The image generations endpoint allows you to create an original image given a text prompt. When using DALL·E 3, images can have a size of 1024x1024, 1024x1792 or 1792x1024 pixels.

By default, images are generated at standard quality, but when using DALL·E 3 you can set quality: "hd" for enhanced detail. Square, standard quality images are the fastest to generate.

You can request 1 image at a time with DALL·E 3 (request more by making parallel requests) or up to 10 images at a time using DALL·E 2 with the n parameter.

if you need any help leodeveloper@gmail.com
