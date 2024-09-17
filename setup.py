from setuptools import setup, find_packages

setup(
    name='Grow-A-Plant',
    version='0.1.0',
    packages=find_packages(where='code'),
    package_dir={'': 'code'},  
    url='https://github.com/layne4fame/Grow-A-Plant',
    license='',  # Specify a license if applicable
    author='Layne Webb, Tegan Wall, Jake Parra',
    author_email='jack.layne.webb@gmail.com',
    description='A Python application developed to run on a Raspberry Pi with sensors to track potential plant growth.',
    install_requires=[
        'adafruit-circuitpython-dht',  # Required dependency
        'gpiozero',  # Required dependency
        'psutil',  # Required dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)
