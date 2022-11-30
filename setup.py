from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name="creategitignore",
    version="0.1",
    description="Create .gitignore files for your projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dapoadedire/gitignore-cli",
    author="Dapo Adedire",
    author_email="<adedireadedapo19@gmail.com>",
    py_modules=["creategitignore"],
    package_dir={"": "src"},
    keywords=["gitignore", "python"],
    install_requires=["colorama"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",



    ],
    entry_points={"console_scripts": ["creategitignore = creategitignore:main"]},
)
