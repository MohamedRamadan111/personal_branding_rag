from app.config import RAGConfig
from app.application import Application


def main() -> None:
    config = RAGConfig(file_path="about_me.txt")
    app = Application(config)
    app.run()


if __name__ == "__main__":
    main()