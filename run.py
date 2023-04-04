from WebApp import create_app, db
from WebApp.models import (
    User,
    Role,
    Farmland,
    Crop,
    HistoricFarmland,
    SoilFarmland,
    Unit,
)

# from flask_ngrok import run_with_ngrok
# from WebApp.models import Role

app = create_app()

# run_with_ngrok(app)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
    # app.run(debug=True)


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "app": app}
