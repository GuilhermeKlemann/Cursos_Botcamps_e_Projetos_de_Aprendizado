from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-test",
    version="0.0.1",
    author="Guilherme Klemann",
    author_email="guilhermeklemanndev@gmail.com",
    description="Pacote de Processamento de imagem.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GuilhermeKlemann/Cursos_Botcamps_e_Projetos_de_Aprendizado/GeraçãoTechUnimedBHCiênciaDeDados/desafio-de-projeto-pacotes-de-processamento-de-imagens-em-Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)