from PIL import Image
import pytesseract

def __init__process():
    text = pytesseract.image_to_string(
        Image.open('E:\\qd_python\\git-python\\python_distinguish\\distinguish\\identify\\process\\image\\timg2.jpg'), 'chi_sim'
    )
    print(text)