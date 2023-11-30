import os

from webapp import create_app


def run_flask():
    app = create_app()
    app.run()

if __name__ == '__main__':
    run_flask()