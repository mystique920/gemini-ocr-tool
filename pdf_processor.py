#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Processor using Gemini OCR
This script converts PDFs to images and processes them using the Gemini OCR functionality.
"""

import argparse
import os
from pathlib import Path
from pdf2image import convert_from_path
import subprocess
import sys

def convert_pdf_to_images(pdf_path, output_dir="images", start_page=1, end_page=None):
    """
    Convert PDF pages to images.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str): Directory to save the images
        start_page (int): First page to convert (1-based)
        end_page (int): Last page to convert (inclusive)
    
    Returns:
        list: List of generated image paths
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get PDF name without extension
    pdf_name = Path(pdf_path).stem
    
    # Convert PDF to images
    images = convert_from_path(pdf_path, first_page=start_page, last_page=end_page)
    
    # Save images and collect paths
    image_paths = []
    for i, image in enumerate(images, start=start_page):
        output_path = Path(output_dir) / f"{pdf_name}_page{i}.png"
        image.save(output_path)
        image_paths.append(str(output_path))
        print(f"Converted page {i} to {output_path}")
    
    return image_paths

def process_pdf_with_gemini(pdf_path, api_key=None, start_page=1, end_page=None, output_dir="output"):
    """
    Process a PDF file using Gemini OCR.
    
    Args:
        pdf_path (str): Path to the PDF file
        api_key (str, optional): Gemini API key
        start_page (int): First page to process
        end_page (int): Last page to process
        output_dir (str): Directory for output images
    """
    # Convert PDF to images
    image_paths = convert_pdf_to_images(pdf_path, start_page=start_page, end_page=end_page)
    
    # Process each image with Gemini OCR
    for image_path in image_paths:
        image_name = os.path.basename(image_path)
        print(f"\nProcessing {image_name}...")
        
        # Build command to run gemini-ocr.py
        cmd = [
            sys.executable,  # Use current Python interpreter
            "gemini-ocr.py",
            "--mode", "ocr",
            "--image-dir", "images",  # Specify the image directory
            "--output-dir", output_dir,
            "--image", image_name  # Pass the specific image to process
        ]
        
        # Add API key if provided
        if api_key:
            cmd.extend(["--api-key", api_key])
        
        # Run the command
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {image_name}: {e}")
            continue

def main():
    parser = argparse.ArgumentParser(description="Process PDF files using Gemini OCR")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--api-key", help="Gemini API key (alternatively, set GOOGLE_API_KEY environment variable)")
    parser.add_argument("--start-page", type=int, default=1, help="First page to process (default: 1)")
    parser.add_argument("--end-page", type=int, help="Last page to process (default: all pages)")
    parser.add_argument("--output-dir", default="output", help="Directory for output images (default: output)")
    
    args = parser.parse_args()
    
    # Process the PDF
    process_pdf_with_gemini(
        args.pdf_path,
        api_key=args.api_key,
        start_page=args.start_page,
        end_page=args.end_page,
        output_dir=args.output_dir
    )

if __name__ == "__main__":
    main() 