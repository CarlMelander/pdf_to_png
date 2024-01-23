from setuptools import setup, find_packages

setup(
    name='PDF_to_PNG',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pillow>=10.2.0',
        'PyMuPDF>=1.23.17'
    ],
    author='Carl Melander',
    author_email='Carl.Melander@Gmail.com',
    description='Convert PDF pages to PNG Images using the Pillow and PyMuPDF Libraries',
)
