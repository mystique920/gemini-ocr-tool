# Gemini OCR Tool

A Python tool that uses Google's Gemini Vision API for OCR (Optical Character Recognition) on images and PDFs. This tool can:

- Extract text from images with bounding boxes
- Process PDF documents page by page
- Support multiple image formats (PNG, JPG, JPEG)
- Provide visual output with text detection boxes

## Features

- **Image OCR**: Process single images to extract text
- **PDF Processing**: Convert PDFs to images and perform OCR on each page
- **Visual Output**: Generate annotated images showing detected text areas
- **Flexible Configuration**: Support for custom API keys, input/output directories, and page ranges

## Requirements

### Python Dependencies
```bash
pip install -r requirements.txt
```

### System Dependencies

For PDF processing, you need to install `poppler`:

- **macOS**:
  ```bash
  brew install poppler
  ```
- **Ubuntu/Debian**:
  ```bash
  sudo apt-get install poppler-utils
  ```
- **Windows**: Download and install poppler from [poppler-windows](http://blog.alivate.com.au/poppler-windows/)

## API Key Setup

Get a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/). You have several options to provide the API key:

1. **Using a .env file (recommended)**:
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

2. **Environment variable**:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

3. **Command line argument**:
   ```bash
   python gemini-ocr.py --api-key "your-api-key-here"
   ```

## Usage

### Image OCR

```bash
# Process a single image
python gemini-ocr.py --mode ocr --image your_image.png

# Specify custom directories
python gemini-ocr.py --mode ocr --image-dir my_images --output-dir results
```

### PDF Processing

```bash
# Process all pages of a PDF
python pdf_processor.py document.pdf

# Process specific pages (e.g., pages 2-4)
python pdf_processor.py document.pdf --start-page 2 --end-page 4

# Specify output directory
python pdf_processor.py document.pdf --output-dir results
```

**Note**: Each page of the PDF requires one API call to Gemini. For large PDFs, consider processing specific pages to manage API usage.

## Output

- Processed images are saved in the `output` directory
- Each processed image shows bounding boxes around detected text areas
- For PDFs, each page is processed separately and saved with a page number suffix

## License

MIT License - feel free to use this tool for any purpose.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 