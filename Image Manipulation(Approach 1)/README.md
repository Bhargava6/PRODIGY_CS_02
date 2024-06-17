It is nothing but a simple process in which we convert our data or information into secret code to prevent it from unauthorized access and keep it private and secure.

First, we will select an image, and then we will convert that image into a byte array due to which the image data will be totally converted into numeric form, and then we can easily apply the XOR operation to it. Now, whenever we will apply the XOR function on each value of the byte array then the data will be changed due to which we will be unable to access it. But we should remember one thing here our encryption key plays a very important role without that key we can not decrypt our image. It acts as a password to decrypt it.

Encryption process:
Here in the above program, as we can see how XOR operation works, it takes two variables data and a key, whenever we perform XOR operation on them for the first time we get encrypted data. Then when we perform the XOR operation between our data and key again, we get the same value as our input variable data (decrypted data). The same logic will be applicable to a byte array of Images during encryption and decryption.

Decryption process:
It is nothing but a process of converting our encrypted data into a readable form. Here we will again apply the same XOR operation on an encrypted image to decrypt it. But always remember that our encryption key and decryption key must be the same.
