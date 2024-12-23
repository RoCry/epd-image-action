import subprocess
import os
from mako.template import Template
from process_image import remap_image, PALETTE_BWR

def render_template(template_path: str, **kwargs) -> str:
    """Render a Mako template with given context"""
    template = Template(filename=template_path)
    return template.render(**kwargs)

def generate_image_for_html(template_path: str, output_path: str, viewport: str, **template_kwargs):
    # Create a temporary rendered HTML file
    temp_html_path = template_path.replace('.html', '_rendered.html')
    
    # Render the template
    rendered_html = render_template(template_path, **template_kwargs)
    
    # Write the rendered HTML to a temporary file
    with open(temp_html_path, 'w') as f:
        f.write(rendered_html)

    # Use Node.js script to generate screenshot
    subprocess.run(
        [
            "node",
            "screenshot.js",
            temp_html_path,
            output_path,
            viewport,
        ],
        check=True,
    )

    # Clean up temporary file
    os.remove(temp_html_path)
    return output_path

def generate_all():
    DIST_FOLDER = "dist/images"
    os.makedirs(DIST_FOLDER, exist_ok=True)

    # Get viewport from environment variable or use default
    viewports = os.environ.get('VIEWPORT_SIZE', '250x122,400x300').split(',')

    # Get all HTML files from htmls directory
    html_files = [f for f in os.listdir("htmls") if f.endswith('.html')]

    for html_file in html_files:
        template_path = os.path.join("htmls", html_file)

        for viewport in viewports:
            output_filename = html_file.replace('.html', f'_{viewport}.png')
            output_path = os.path.join(DIST_FOLDER, output_filename)
            output_path = generate_image_for_html(
                template_path,
                output_path,
                viewport
            )
            # generate a binary jpg for openepaperlink(which only supports jpg for now)
            binary_output_path = output_path.replace('.png', '.jpg')
            # TODO: hardcode the palette for now
            remap_image(output_path, binary_output_path, palette=PALETTE_BWR)
            print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_all()
