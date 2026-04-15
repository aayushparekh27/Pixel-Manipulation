from PIL import Image
import os

def encrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Simple encryption using XOR with key
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        encrypted_path = "encrypted_" + os.path.basename(image_path)
        img.save(encrypted_path)
        print("Image encrypted and saved as:", encrypted_path)

    except Exception as e:
        print("Encryption error:", e)


def decrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Decryption is same as encryption (XOR again)
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        decrypted_path = "decrypted_" + os.path.basename(image_path)
        img.save(decrypted_path)
        print("Image decrypted and saved as:", decrypted_path)

    except Exception as e:
        print("Decryption error:", e)


def main():
    print("=== Pixel Manipulation Image Encryptor ===")
    while True:
        choice = input("\nChoose 'encrypt', 'decrypt' or 'exit': ").strip().lower()
        if choice == 'exit':
            break
        elif choice not in ['encrypt', 'decrypt']:
            print("Invalid choice.")
            continue

        image_path = input("Enter image file path: ")
        if not os.path.exists(image_path):
            print("File not found.")
            continue

        try:
            key = int(input("Enter numeric key (0-255): "))
            if key < 0 or key > 255:
                print("Key must be between 0 and 255.")
                continue
        except ValueError:
            print("Invalid key.")
            continue

        if choice == 'encrypt':
            encrypt_image(image_path, key)
        else:
            decrypt_image(image_path, key)

if __name__ == "__main__":
    main()
