import qrcode

def qrcode_generator():
    """
    Welcomes the user to the QR Code Generator
    Asks for the type of QR Code they want to generate
    Whether url, text, etc.
    """
    while True:
        print("""Welcome to the QR Code Generator
        1. URL
        2. Text
        """)
        qr_type = int(input("Select the type of QR Code you would like to generate: "))
        if qr_type == 1:
            url = input("Enter the URL: ")
            qr = qrcode.make(url)
            qr.save("url.png")
            print("Go to this location for the QR Code")
            print(r"C:\Users\JAMES\PycharmProjects\Projects\QRCode Generator")
            break
        elif qr_type == 2:
            text = input("Enter the Text: ")
            qr = qrcode.make(text)
            qr.save("text.png")
            print("Go to this location for the QR Code")
            print(r"C:\Users\JAMES\PycharmProjects\Projects\QRCode Generator")
            break
        else:
            print("Invalid Input: Try Again: ")
    return



if __name__ == "__main__":
    qrcode_generator()

