import subprocess
import os
from mako.template import Template
from process_image import remap_image, PALETTE_BWR

def render_template(template_path: str, **kwargs) -> str:
    """Render a Mako template with given context"""
    template = Template(filename=template_path)
    return template.render(**kwargs)

def generate_image_for_html(template_path: str, output_path: str, viewport: str, **template_kwargs):
    # Create rendered HTML file in dist/htmls
    dist_html_dir = "dist/htmls"
    os.makedirs(dist_html_dir, exist_ok=True)
    rendered_html_path = os.path.join(dist_html_dir, os.path.basename(template_path).replace('.html', '_rendered.html'))
    
    # Render the template
    rendered_html = render_template(template_path, **template_kwargs)
    
    # Write the rendered HTML to the dist folder
    with open(rendered_html_path, 'w') as f:
        f.write(rendered_html)

    # Use Node.js script to generate screenshot
    subprocess.run(
        [
            "node",
            "screenshot.js",
            rendered_html_path,
            output_path,
            viewport,
        ],
        check=True,
    )

    return output_path

def generate_all():
    DIST_FOLDER = "dist/images"
    os.makedirs(DIST_FOLDER, exist_ok=True)

    # Get viewport from environment variable or use default
    viewports = os.environ.get('VIEWPORT_SIZE', '250x122,400x300').split(',')
    # when debug, we may only want to generate some specific templates
    whitelist_keyword = os.environ.get('WHITELIST')

    # Get all HTML files from htmls directory
    html_files = [f for f in os.listdir("htmls") if f.endswith('.html')]

    for html_file in html_files:
        if whitelist_keyword and whitelist_keyword not in html_file:
            continue
        template_path = os.path.join("htmls", html_file)

        for viewport in viewports:
            output_filename = html_file.replace('.html', f'_{viewport}.png')
            output_path = os.path.join(DIST_FOLDER, output_filename)
            try:
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
            except Exception as e:
                print(f"Error generating {output_path}: {str(e)}")
                continue

if __name__ == "__main__":
    generate_all()
