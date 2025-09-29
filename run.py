import os
from app import create_app, db  # 👈 import db as well

app = create_app()

if __name__ == "__main__":
    # Create all tables (only if they don't exist yet)
    with app.app_context():
        db.create_all()

    debug_mode = os.environ.get("FLASK_DEBUG", "True").lower() == "true"
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "127.0.0.1")

    print("Backend is starting")
    print(f"The backend is running on http://{host}:{port}")  # 👈 fixed f-string

    app.run(host=host, port=port, debug=debug_mode, threaded=True)
