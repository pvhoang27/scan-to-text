import pytesseract
from PIL import Image
import os

# Chỉ rõ đường dẫn tới file tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Chỉ rõ đường dẫn tới thư mục tessdata
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

def scan_to_text(image_path, output_folder="output"):
    # Tạo folder nếu chưa có
    os.makedirs(output_folder, exist_ok=True)

    # OCR
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='vie')

    # Tạo tên file txt cùng tên với ảnh
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = os.path.join(output_folder, f"{base_name}.txt")

    # Lưu text ra file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return output_path

if __name__ == "__main__":
    file = "processed.jpg"
    output_file = scan_to_text(file)
    print(f"Nội dung đã lưu tại: {output_file}")
