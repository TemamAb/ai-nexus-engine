from setuptools import setup, find_packages

setup(
    name="ai-nexus-engine",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn[standard]==0.24.0",
        "web3==6.11.0",
        "numpy==1.26.4",
        "pandas==2.2.1",
        "scikit-learn==1.4.1.post1",
    ],
    python_requires=">=3.8,<3.12",
)
