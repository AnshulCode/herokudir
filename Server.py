from flask import Flask

Server = Flask(__name__)

@Server.route('/')
def main():
    return 'hello world'

if __name__ == '__main__':
    Server.run()