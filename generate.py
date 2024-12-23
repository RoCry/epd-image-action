import pathlib
import subprocess
import tempfile
import os

def generate_image_for_html(html_path: str, output_path: str, viewport: str):
    # TODO: when using puppeteer screenshot, the font seems doesnt load success sometimes
    # change it to use js script to generate the image
    subprocess.run(
        [
            "puppeteer",
            "screenshot",
            html_path,
            output_path,
            "--viewport",
            viewport,
        ],
    )
    return output_path

def generate_all():
    DIST_FOLDER = "dist/images"
    os.makedirs(DIST_FOLDER, exist_ok=True)
    output_path = generate_image_for_html("htmls/hello.html", f"{DIST_FOLDER}/hello.png", "250x122")
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_all()