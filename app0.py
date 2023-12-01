# import os

# from webapp import create_app


# def run_flask():
#     app = create_app()
#     app.run()
#     return app

# if __name__ == '__main__':
#     run_flask()



from webapp import create_app


app = create_app()

if __name__ == '__main__':
    app.run()