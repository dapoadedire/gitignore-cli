from setuptools import setup


setup(
    name="creategitignore",
    version="0.0.1",
    description="Create .gitignore files for your projects",
    url="htts://github.com/dapoadedire/gitignore-cli",
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
    ],
    entry_points={"console_scripts": ["creategitignore = creategitignore:main"]},
)
