import setuptools 

# with open("README.md", "r", encoding= "utf-8") as f:
#     long_description = f.read()


__version__ = "1.0.0"

REPO_NAME = "Chatbot"
AUTHOR_USER_NAME = "45hv1n"
SRC_REPO = "Chatbot"
AUTHOR_EMAIL = "helloWorld@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Chatbot Project",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)