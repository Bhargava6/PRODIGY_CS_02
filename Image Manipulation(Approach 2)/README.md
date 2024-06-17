Explanation:
Function encrypt_decrypt_image:

Input: image_path (path to the image file), key (an integer for the XOR operation), mode (either 'encrypt' or 'decrypt').
Process:
Open the image using the Pillow library.
Convert the image to RGB format.
Convert the image to a NumPy array for pixel manipulation.
Apply the XOR operation with the provided key to each pixel.
Create a new image from the modified pixel array.
Output: Returns the encrypted or decrypted image.

Main Program:

Prompts the user to enter the image file path, the key, and the mode (either 'encrypt' or 'decrypt').
Calls the encrypt_decrypt_image function with the provided inputs.
Saves the result image as "encrypted_image.png" or "decrypted_image.png" based on the selected mode.

Encrypt an Image:

Run the program and enter the image path, an integer key, and 'encrypt' mode.
The encrypted image will be saved as "encrypted_image.png".

Decrypt an Image:

Run the program and enter the path to the encrypted image, the same integer key used for encryption, and 'decrypt' mode.
The decrypted image will be saved as "decrypted_image.png".
