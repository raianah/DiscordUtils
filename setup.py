import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DisnakeUtils",
    version="1.3.4",
    author="toxicrecker, raianah",
    description="DisnakeUtils is a forked library from toxicrecker, made for compatibility purposes in disnake.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/raianah/DisnakeUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">= 3.6",
    include_package_data=True,
    install_requires=["disnake"],
    extras_require={"voice": ["disnake[voice]", "youtube-dl"]}
)
