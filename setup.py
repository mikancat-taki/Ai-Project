from setuptools import setup, find_packages

setup(
    name='ai-desktop-app',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A desktop application for AI model inference and interaction.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ai-desktop-app',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project's dependencies here
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',  # or 'torch' depending on your model
        'flask',  # if you're using Flask for the API
        # Add other dependencies as needed
    ],
    entry_points={
        'console_scripts': [
            'ai-desktop-app=main:main',  # Adjust based on your main function
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)