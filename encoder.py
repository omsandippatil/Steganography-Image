from PIL import Image
import numpy as np
import os

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encode_image(image_path, text):
    # Open the image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img)

    # Flatten the array
    flat_array = img_array.flatten()

    # Convert text to binary
    binary_text = text_to_binary(text)
    
    if len(binary_text) > len(flat_array):
        raise ValueError("Text is too long to be encoded in this image")

    # Add delimiter to know where the message ends
    binary_text += '00000000'

    # Modify the least significant bits
    for i, bit in enumerate(binary_text):
        flat_array[i] = (flat_array[i] & 0xFE) | int(bit)

    # Reshape the array back to 2D/3D
    encoded_array = flat_array.reshape(img_array.shape)

    # Create a new image from the modified array
    encoded_img = Image.fromarray(encoded_array.astype('uint8'), img.mode)
    
    # Generate output filename
    directory, filename = os.path.split(image_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(directory, f"{name}_encoded{ext}")
    
    # Save the encoded image
    encoded_img.save(output_path)
    return output_path

def get_user_input():
    input_image = input("Enter the path of the input image: ")
    secret_text = input("Enter the secret message: ")
    return input_image, secret_text

if __name__ == "__main__":
    print("Welcome to the Image Steganography Encoder!")
    input_image, secret_text = get_user_input()

    try:
        # Encode the message
        output_path = encode_image(input_image, secret_text)
        print(f"Encoding successful! Encoded image saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")