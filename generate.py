import pathlib
import subprocess
import tempfile
import os

def put_github_action_env(key: str, value: str):
    env_file = os.getenv("GITHUB_ENV")
    if env_file is None:
        # Local development - just print the value
        print(f"Local development: Would set {key}={value}")
        return
    
    # Running in GitHub Actions
    with open(env_file, "a") as f:
        f.write(f"{key}<<EOF\n{value}\nEOF\n")

def generate_image_for_html(html_path: str, output_path: str, viewport: str):
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
    DIST_FOLDER = "dist"
    os.makedirs(DIST_FOLDER, exist_ok=True)
    output_path = generate_image_for_html("htmls/hello.html", f"{DIST_FOLDER}/hello.png", "250x122")
    print(f"Generated {output_path}")
    put_github_action_env("IMAGES_FILES", output_path)

if __name__ == "__main__":
    generate_all()