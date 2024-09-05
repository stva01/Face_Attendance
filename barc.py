# import cv2
# from pyzbar.pyzbar import decode

# def barcode_scanner(image_path):
#     # Read the input image
#     image = cv2.imread(image_path)

#     # Convert the image to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Use the pyzbar library to decode barcodes
#     barcodes = decode(gray)

#     # Loop through detected barcodes
#     for barcode in barcodes:
#         # Extract the barcode data
#         barcode_data = barcode.data.decode("utf-8")

#         # Draw a rectangle around the barcode
#         points = barcode.polygon
#         if len(points) == 4:
#             hull = cv2.convexHull(points)
#             cv2.polylines(image, [hull], True, (0, 255, 0), 2)

#         # Display the barcode data
#         print(f"Barcode Data: {barcode_data}")

#     # Display the image with the detected barcodes
#     cv2.imshow("Barcode Scanner", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     # Replace 'your_image_path.jpg' with the path to your barcode image
#     barcode_scanner(r'C:\Users\Romil Shah\Desktop\Attendance PY MP\image\barcode.jpeg')
    
    



import cv2
from pyzbar.pyzbar import decode

def barcode_scanner(image_path):
    # Read the input image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use the pyzbar library to decode barcodes
    barcodes = decode(gray)

    # Loop through detected barcodes
    for barcode in barcodes:
        # Extract the barcode data
        barcode_data = barcode.data.decode("utf-8")

        # Draw a rectangle around the barcode
        points = barcode.polygon
        if len(points) == 4:
            hull = cv2.convexHull(points)
            cv2.polylines(image, [hull], True, (0, 255, 0), 2)

        # Display the barcode data
        print(f"Original Barcode Data: {barcode_data}")

        # Extract and display only numerical digits from the barcode
        digits = ''.join(filter(str.isdigit, barcode_data))
        print(f"Extracted Digits: {digits}")

    # Display the image with the detected barcodes
    cv2.imshow("Barcode Scanner", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Use double backslashes or a raw string to avoid the 'unicodeescape' error
    barcode_scanner('C:\\Users\\Romil Shah\\Desktop\\Attendance PY MP\\image\\barcode.jpeg')
    # Or
    # barcode_scanner(r'C:\Users\Romil Shah\Desktop\Attendance PY MP\image\barcode.jpeg')

