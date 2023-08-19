import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='model_registry',
    author='Rakveer Chand',
    author_email='rakveerchand@gmail.com',
    description='Model Registry PyPI (Python Package Index) Package',
    keywords='model_registry, pypi, sagemaker',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Rakveerchand/model_registry',
    project_urls={
        'Documentation': 'https://github.com/Rakveerchand/model_registry',
        'Bug Reports': 'https://github.com/Rakveerchand/model_registry/issues',
        'Source Code': 'https://github.com/Rakveerchand/model_registry',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['boto3==1.28.10', 'sagemaker==2.178.0',"botocore==1.4.1","s3transfer==0.1.0","sagemaker==2.178.0"],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
