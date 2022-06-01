from website import create_app
from website.models.DataBase import DataBase

app = create_app()

if __name__ == '__main__':
    db = DataBase.create();

    app.run(debug=True)