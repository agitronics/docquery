import os
import setuptools
import sys

dir_name = os.path.abspath(os.path.dirname(__file__))

version_contents = {}
with open(os.path.join(dir_name, "src", "docqa", "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

with open(os.path.join(dir_name, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()

install_requires = [
    "torch >= 1.0",
    "transformers >= 4.18.0",
    # TODO: These could potentially be captured as an extra
    "Pillow",
    "pydantic",
    "pytesseract",  # TODO: Test what happens if the host machine does not have tesseract installed
    "requests",
]
extras_require = {
    "dev": [
        "black",
        "build",
    ],
    "cli": [],
}
extras_require["all"] = sorted({package for packages in extras_require.values() for package in packages})

setuptools.setup(
    name="docqa",
    version=version_contents["VERSION"],
    author="Impira Engineering",
    author_email="engineering@impira.com",
    description="DocQA: An easy way to extract information from documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/impira/docqa",
    project_urls={
        "Bug Tracker": "https://github.com/impira/docqa/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8.0",
    entry_points={
        "console_scripts": ["docqa = docqa.cmd.__main__:main"],
    },
    install_requires=install_requires,
    extras_require=extras_require,
)