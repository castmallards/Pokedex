from Blueprints import create_app # importing __init__.py's create app

app = create_app()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')