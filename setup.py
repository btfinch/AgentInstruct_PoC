from setuptools import setup, find_packages

setup(
    name="AgentInstruct_PoC",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "datasets",
        "openai",
        "python-dotenv",
        "scikit-learn",
        "numpy",
        "autogen",
        "pyautogen",  # Add this line
    ],
)