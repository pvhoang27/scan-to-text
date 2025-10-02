import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

def preprocess_image(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path)

    # Chuyển thành ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Làm rõ chữ bằng threshold
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Trả về ảnh đã xử lý
    return thresh

def scan_to_text(image_path, lang='vie'):
    img = preprocess_image(image_path)
    text = pytesseract.image_to_string(img, lang=lang)
    return text

if __name__ == "__main__":
    file = "sddefault.jpg"
    result = scan_to_text(file)
    print("Kết quả OCR cải thiện:")
    print(result)
