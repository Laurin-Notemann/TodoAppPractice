from Connection.Connection import create_table
from server.server import app


def main():
    create_table()
    app.run(debug=True)
    
main()
