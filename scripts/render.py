import sys
import subprocess
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def render_script(script_path):
    with open(script_path, "r") as script_file:
        script = script_file.read()

    highlighted_code = highlight(script, PythonLexer(), HtmlFormatter())

    output = subprocess.run(["python", script_path], capture_output=True, text=True)
    stdout = output.stdout
    stderr = output.stderr

    return highlighted_code, stdout, stderr

if __name__ == "__main__":
    script_path = sys.argv[1]
    highlighted_code, stdout, stderr = render_script(script_path)

    with open("output.html", "w") as output_file:
        output_file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Notebook-like Output</title>
    <style>
        {HtmlFormatter().get_style_defs('.highlight')}
        pre {{
            background-color: #f8f8f8;
            padding: 0.5em;
            border-radius: 5px;
            overflow-x: auto;
        }}
        .output {{
            border: 1px solid #ccc;
            background-color: #f8f8f8;
            padding: 0.5em;
            border-radius: 5px;
            white-space: pre-wrap;
        }}
    </style>
</head>
<body>
    <h1>Code:</h1>
    <div class="code">
        {highlighted_code}
    </div>
    <h1>Output:</h1>
    <div class="output">
        {stdout}
    </div>
    <h1>Error (if any):</h1>
    <div class="output">
        {stderr}
    </div>
</body>
</html>
        """)
