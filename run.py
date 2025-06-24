from app import create_app  # type: ignore # This assumes app/__init__.py defines create_app()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Optional: add debug=True for development
