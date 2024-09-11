
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import pytesseract
from io import BytesIO


app = FastAPI()

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

@app.post("/ask_gpt/upload_img")
async def extract_text(file: UploadFile = File(...)):
    
    image_bytes = await file.read()
    
    img = Image.open(BytesIO(image_bytes))
    
    extracted_text = extract_text_from_image(img)
    print(extracted_text)
    return {"text": extracted_text}
