from setuptools import setup, find_packages

setup(
    name='noorTest',         # How you named your package folder (MyLib)
    packages=find_packages(),       # Automatically find and include all packages
    version='0.1',                  # Start with a small number and increase it with every change you make
    license='MIT',                  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
    author='Noor',             # Type in your name
    author_email='noormohideen61@gmail.com',  # Type in your E-Mail
    url='https://github.com/user/reponame',  # Provide either the link to your github or to your website
    # download_url='https://github.com/Noor-Mohideen-S/valeiraConnect/archive/refs/tags/v_01.tar.gz',  # I explain this later on
    keywords=['SOME', 'MEANINGFUL', 'KEYWORDS'],  # Keywords that define your package best
    install_requires=[              # I get to this in a second
        'openai',        
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which Python versions you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',  # Placeholder for future Python 3.12
        # 'Programming Language :: Python :: 3.13',  # Placeholder for future Python 3.13
    ],
)
