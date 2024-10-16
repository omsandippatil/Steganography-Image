from PIL import Image
import numpy as np

def decode_image(image_path):
    # Open the encoded image
    img = Image.open(image_path)
    # Convert image to numpy array
    img_array = np.array(img)

    # Flatten the array
    flat_array = img_array.flatten()

    # Extract the least significant bits
    binary_text = ''.join([str(pixel & 1) for pixel in flat_array])

    # Convert binary to text
    decoded_text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        if byte == '00000000':  # Stop when we reach the delimiter
            break
        decoded_text += chr(int(byte, 2))

    return decoded_text

def get_user_input():
    encoded_image = input("Enter the path of the encoded image: ")
    return encoded_image

if __name__ == "__main__":
    print("Welcome to the Image Steganography Decoder!")
    encoded_image = get_user_input()

    try:
        # Decode the message
        decoded_message = decode_image(encoded_image)
        print(f"Decoded message: {decoded_message}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")