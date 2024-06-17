from PIL import Image
import numpy as np
import random

def generate_permutation_indices(width, height, key):
    # Initialize the random number generator with the key
    random.seed(key)
    # Generate a list of all pixel indices
    indices = [(x, y) for x in range(width) for y in range(height)]
    # Shuffle the indices randomly
    random.shuffle(indices)
    return indices

def encrypt_decrypt_image(image_path, key, mode):
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure image is in RGB format
    width, height = img.size
    img_array = np.array(img)

    # Generate permutation indices based on the key
    permutation_indices = generate_permutation_indices(width, height, key)

    # Create an array to hold the encrypted/decrypted image
    encrypted_decrypted_array = np.zeros_like(img_array)

    if mode == 'encrypt':
        for i, (x, y) in enumerate(permutation_indices):
            # Get the original pixel position
            original_x = i % width
            original_y = i // width
            # Assign the pixel value to the new position
            encrypted_decrypted_array[x, y] = img_array[original_y, original_x]
    elif mode == 'decrypt':
        for i, (x, y) in enumerate(permutation_indices):
            # Get the original pixel position
            original_x = i % width
            original_y = i // width
            # Assign the pixel value from the encrypted position back to the original position
            encrypted_decrypted_array[original_y, original_x] = img_array[x, y]

    # Create a new image from the modified array
    encrypted_decrypted_img = Image.fromarray(encrypted_decrypted_array.astype(np.uint8))
    return encrypted_decrypted_img

if __name__ == "__main__":
    # User inputs
    image_path = input("Enter the path to the image file: ")
    key = input("Enter the encryption/decryption key (an integer): ")
    mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected.")
    else:
        result_img = encrypt_decrypt_image(image_path, int(key), mode)
        output_path = "encrypted_image.png" if mode == 'encrypt' else "decrypted_image.png"
        result_img.save(output_path)
        print(f"Image has been {mode}ed and saved as {output_path}")
