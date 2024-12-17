from setuptools import setup, find_packages

setup(
    name='custom-vector-store',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'vector-store=vector_store.vector_store:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A custom vector store for efficient vector operations and similarity search.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/custom-vector-store',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)