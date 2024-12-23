import pathlib
import subprocess
import tempfile
import os

def generate_image_for_html(html_path: str, output_path: str, viewport: str):
    # Use Node.js script to generate screenshot
    subprocess.run(
        [
            "node",
            "screenshot.js",
            html_path,
            output_path,
            viewport,
        ],
        check=True,  # This will raise an exception if the command fails
    )
    return output_path

def generate_all():
    DIST_FOLDER = "dist/images"
    os.makedirs(DIST_FOLDER, exist_ok=True)
    output_path = generate_image_for_html("htmls/hello.html", f"{DIST_FOLDER}/hello.png", "250x122")
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_all()