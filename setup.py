from setuptools import setup, find_packages

setup(
    name='flet-toast',
    version='0.3.0',
    author='Web Tech Moz',
    author_email='zoidycine@gmail.com',
    description='Cria interface para exibir notificações na tela',
    long_description=open('README.md', 'r', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/webtechmoz/flet-toast.git',
    packages=find_packages(),
    keywords=['toastfy', 'toasty-flet', 'flet-toast', 'toast', 'flet'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)