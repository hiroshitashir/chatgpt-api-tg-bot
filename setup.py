from setuptools import setup, find_packages

setup(
    name="chatgpt_bot",
    version="0.0.1",
    description="Generic Telegram bot using ChatGPT API",
    url="https://github.com/hiroshitashir/chatgpt-api-tg-bot",
    author="Hiroshi Tashiro",
    author_email="hiroshitashir@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
