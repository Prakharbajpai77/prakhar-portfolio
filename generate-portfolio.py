import os
from zipfile import ZipFile

# Directory setup
os.makedirs("prakhar_portfolio/assets/css", exist_ok=True)

# HTML content
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prakhar Bajpai | Portfolio</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header>
        <h1>Prakhar Bajpai</h1>
        <p>Web Developer & Software Developer</p>
    </header>
    <section class="about">
        <h2>About Me</h2>
        <p>I’m Prakhar, a passionate developer skilled in Java, Python, HTML/CSS/JS, C, and C++. Inspired by MS Dhoni, I aim to build reliable, smart, and effective software solutions.</p>
    </section>
    <section class="skills">
        <h2>Skills</h2>
        <ul>
            <li>Java</li>
            <li>Python</li>
            <li>HTML/CSS/JavaScript</li>
            <li>C</li>
            <li>C++</li>
        </ul>
    </section>
    <section class="contact">
        <h2>Contact Me</h2>
        <p>Email: <a href="mailto:prakharbajpai727504@gmail.com">prakharbajpai727504@gmail.com</a></p>
    </section>
    <footer>
        <p>&copy; 2025 Prakhar Bajpai. Inspired by MS Dhoni.</p>
    </footer>
</body>
</html>
"""

# CSS content
style_css = """body {
    margin: 0;
    font-family: 'Segoe UI', sans-serif;
    background-color: #121212;
    color: #f1f1f1;
    line-height: 1.6;
}
header {
    text-align: center;
    padding: 2rem;
    background: #1e1e1e;
}
header h1 {
    margin: 0;
    font-size: 2.5rem;
}
header p {
    font-size: 1.2rem;
    color: #bbbbbb;
}
section {
    padding: 2rem;
    max-width: 800px;
    margin: auto;
}
.skills ul {
    list-style: none;
    padding: 0;
}
.skills li {
    background: #1f1f1f;
    margin: 0.5rem 0;
    padding: 0.5rem;
    border-radius: 4px;
}
a {
    color: #4fc3f7;
}
footer {
    text-align: center;
    padding: 1rem;
    background: #1e1e1e;
    font-size: 0.9rem;
    color: #777;
}
"""

# Write files
with open("prakhar_portfolio/index.html", "w") as f:
    f.write(index_html)

with open("prakhar_portfolio/assets/css/style.css", "w") as f:
    f.write(style_css)

# Create zip file
with ZipFile("prakhar_portfolio.zip", "w") as zipf:
    for foldername, _, filenames in os.walk("prakhar_portfolio"):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            zipf.write(filepath, os.path.relpath(filepath, "prakhar_portfolio"))
