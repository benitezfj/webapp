from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from WebApp import db, bcrypt
from WebApp.forms import (
    RegistrationForm,
    LoginForm,
    RegistrationRoleForm,
    MapForm,
    RegistrationCropForm,
    FertilizarMapForm,
    InsertHistoricalForm,
    SoilForm,
    InsertFarmlandForm,
    CalculatorForm,
)
from WebApp.models import (
    User,
    Role,
    Farmland,
    Crop,
    HistoricFarmland,
    SoilFarmland,
    Unit,
)
from fertilizer.calculator_spinach import spinachFertilizer
from fertilizer.calculateBlend import calculateBlend
from earthengine.methods import get_image_collection_asset, get_fertilizer_map
from config import Config

import numpy as np
import datetime as dt
import ee
from ee.ee_exception import EEException

if Config.EE_ACCOUNT:
    try:
        credentials = ee.ServiceAccountCredentials(
            Config.EE_ACCOUNT, Config.EE_PRIVATE_KEY_FILE
        )
        ee.Initialize(credentials)
    except EEException as e:
        print(str(e))
else:
    ee.Initialize()

# earthengine authenticate
# ee.Initialize()
# try:
#         ee.Initialize()
# except Exception as e:
#         ee.Authenticate()
#         ee.Initialize()

# try:
#     ee.Initialize()
# except Exception as e:
#     EE_CREDENTIALS = ee.ServiceAccountCredentials(Config.EE_ACCOUNT, Config.EE_PRIVATE_KEY_FILE)
#     ee.Initialize(EE_CREDENTIALS)

# from config import Config
# EE_CREDENTIALS = ee.ServiceAccountCredentials(config.EE_ACCOUNT, config.EE_PRIVATE_KEY_FILE)
# ee.Initialize(EE_CREDENTIALS)

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    if not current_user.is_authenticated:
        return redirect(url_for("main.login"))
    return render_template("home.html")


@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = RegistrationForm()
    pos = [(p.id, p.description) for p in Role.query.order_by(Role.description).all()]
    form.role.choices = pos
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data,
            email=form.email.data,
            role_id=form.role.data,
            password=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        flash("You have successfully registered.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html", title="Register", form=form)


@main.route("/newrole", methods=["GET", "POST"])
@login_required
def registerrole():
    form = RegistrationRoleForm()
    if form.validate_on_submit():
        pos = Role(description=form.description.data)
        db.session.add(pos)
        db.session.commit()
        flash("A new role has been registered", "success")
        return redirect(url_for("main.login"))
    return render_template("position.html", title="Role", form=form)


@main.route("/newcrop", methods=["GET", "POST"])
@login_required
def registercrop():
    form = RegistrationCropForm()
    if form.validate_on_submit():
        pos = Crop(description=form.description.data)
        db.session.add(pos)
        db.session.commit()
        flash("A new crop type has been registered.", "success")
        return redirect(url_for("main.login"))
    return render_template("croptype.html", title="Crop", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():
    # Redireccionaar a /list
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))


@main.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")


@main.route("/farmlandlist")
@login_required
def land_selection():
    lands = (
        db.session.query(Farmland)
        .join(Crop)
        .add_columns(
            Farmland.id,
            Farmland.name,
            Crop.description,
            Farmland.sow_date,
            Farmland.harvest_date,
            Farmland.product_expected,
            Farmland.coordinates,
        )
        .filter(Farmland.croptype_id == Crop.id)
    )
    return render_template("land_selection.html", title="Farmland List", lands=lands)


@main.route("/about")
def about():
    return render_template("about.html", title="About")


@main.route("/vegetationindex", methods=["GET", "POST"])
@login_required
def maps():
    form = MapForm()
    # user = User.query.get_or_404(current_user.get_id())
    form.farmland.choices = [
        (f.id, f.name) for f in Farmland.query.order_by(Farmland.name).all()
    ]

    # form.farmland.choices = [(f.id, f.name) for f in Farmland.query.order_by(Farmland.name).filter(user_id==user).all()]

    if form.validate_on_submit():
        farm_id = form.farmland.data
        index = form.indices.data
        index_date = form.index_date.data
        coverage = 60

        index_date = index_date.strftime("%Y-%m-%d")

        lands = Farmland.query.get_or_404(farm_id)
        farmland_name = lands.name
        coord = np.array(lands.coordinates.split(","))

        roi = ee.Geometry.Polygon([float(i) for i in coord])
        lon = ee.Number(roi.centroid().coordinates().get(0)).getInfo()
        lat = ee.Number(roi.centroid().coordinates().get(1)).getInfo()

        map_url, index_name, end_date = get_image_collection_asset(
            platform="sentinel",
            sensor="2",
            product="BOA",
            cloudy=coverage,
            date_to=index_date,
            roi=roi,
            index=index,
        )

        map_json = {
            "map_url": map_url,
            "latitude": lat,
            "longitude": lon,
            "farmland_name": farmland_name,
            "index_name": index_name,
            "indexdate": end_date,
            "cover": coverage,
        }

        return render_template(
            "results.html", title="Vegetation Index", maps=map_json, form=form
        )
    return render_template("input.html", title="Vegetation Index", form=form)


@main.route("/fertilizermap", methods=["GET", "POST"])
@login_required
def fertilizer_maps():
    form = FertilizarMapForm()
    # user = User.query.get_or_404(current_user.get_id())
    form.farmland.choices = [
        (f.id, f.name) for f in Farmland.query.order_by(Farmland.name).all()
    ]
    # form.farmland.choices = [(f.id, f.name) for f in Farmland.query.order_by(Farmland.name).filter(user_id==user).all()]

    if form.validate_on_submit():
        farm_id = form.farmland.data

        coverage = 60
        lands = Farmland.query.get_or_404(farm_id)
        farmland_name = lands.name
        coord = np.array(lands.coordinates.split(","))
        production_exp = lands.product_expected

        roi = ee.Geometry.Polygon([float(i) for i in coord])
        lon = ee.Number(roi.centroid().coordinates().get(0)).getInfo()
        lat = ee.Number(roi.centroid().coordinates().get(1)).getInfo()

        nutrients = spinachFertilizer(production_exp)
        nitrogen, potassium, phosphorus = nutrients[0:3]

        amount_fertilizer, type_fertilizer, diff_blend = calculateBlend(
            n=nitrogen, p=potassium, k=phosphorus, db=2
        )

        type_fertilizer = np.array(type_fertilizer)
        type_fertilizer = type_fertilizer.astype(int)

        b = [0.7, 1, 1.1]

        amount_fertilizer = np.outer(np.array(b), np.array(amount_fertilizer))

        fertilizer_color = ["#027100", "#88fa4d", "#f17200"]

        map_url, end_date = get_fertilizer_map(
            platform="sentinel",
            sensor="2",
            product="BOA",
            cloudy=coverage,
            roi=roi,
            reducer="first",
        )

        map_json = {
            "map_url": map_url,
            "latitude": lat,
            "longitude": lon,
            "farmland_name": farmland_name,
            "posologydate": end_date,
            "production_exp": production_exp,
        }

        return render_template(
            "results_fertilizer.html",
            title="Maps",
            maps=map_json,
            form=form,
            nutrient=nutrients,
            amount_fertilizer=amount_fertilizer,
            type_fertilizer=type_fertilizer,
            fertilizer_color=fertilizer_color,
            prod_exp=production_exp,
        )
    return render_template("input_fertilizer.html", title="Maps", form=form)


@main.route("/calculator", methods=["GET", "POST"])
@login_required
def calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        nitro = form.nitrogen.data
        phosp = form.phosphorus.data
        pota = form.potassium.data

        amount_fertilizer, type_fertilizer, diff_blend = calculateBlend(
            n=nitro, p=phosp, k=pota, db=2
        )

        myDict = {}
        for i in range(0, len(amount_fertilizer)):
            myDict[i] = [amount_fertilizer[i]]
            myDict[i].append(type_fertilizer[i])

        return render_template(
            "results_calculator.html",
            title="Sanzar Calculator",
            form=form,
            fertilizer_measure=myDict,
        )
    return render_template(
        "input_calculator.html", title="Sanzar Calculator", form=form
    )


@main.route("/inserthistoric", methods=["GET", "POST"])
@login_required
def insert_historical_data():
    form = InsertHistoricalForm()
    # user = User.query.get_or_404(current_user.get_id())
    form.current_farm.choices = [
        (f.id, f.name)
        for f in Farmland.query.order_by(Farmland.name)
        .filter(
            Farmland.harvest_date
            > dt.date(
                dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day
            )
        )
        .all()
    ]

    # form.current_farm.choices = [(f.id, f.name) for f in Farmland.query.order_by(Farmland.name).filter(Farmland.harvest_date > dt.date(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day),user_id==user).all()]

    form.croptype1.choices = [
        (c.id, c.description) for c in Crop.query.order_by(Crop.description).all()
    ]

    if form.validate_on_submit():

        hist = HistoricFarmland(
            current_farm_id=form.current_farm.data,
            croptype_id=form.croptype1.data,
            sow_date=form.sowdate1.data,
            harvest_date=form.harvestdate1.data,
            product_obtained=form.productobtained.data,
            nitrogen_type1=form.nitrogen1.data,
            phosphorus_type1=form.phosphorus1.data,
            potassium_type1=form.potassium1.data,
            posology_type1=form.posology1.data,
            nitrogen_type2=form.nitrogen2.data,
            phosphorus_type2=form.phosphorus2.data,
            potassium_type2=form.potassium2.data,
            posology_type2=form.posology2.data,
            nitrogen_type3=form.nitrogen3.data,
            phosphorus_type3=form.phosphorus3.data,
            potassium_type3=form.potassium3.data,
            posology_type3=form.posology3.data,
            diseases_abnormalities=form.diseasesabnormalities.data,
            diseases_abnormalitiesdate=form.diseasesabnormalitiesdate.data,
            observation=form.treatmentobservation.data,
        )
        # user_id=user,

        db.session.add(hist)
        db.session.commit()
        flash("A historical farmland was assigned to a current one.", "success")
        return redirect(url_for("main.login"))
    return render_template("historical.html", title="Historical", form=form)


@main.route("/soiltest", methods=["GET", "POST"])
@login_required
def insert_soiltest():
    form = SoilForm()
    # user = User.query.get_or_404(current_user.get_id())
    form.current_farm.choices = [
        (f.id, f.name)
        for f in Farmland.query.order_by(Farmland.name)
        .filter(
            Farmland.harvest_date
            > dt.date(
                dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day
            )
        )
        .all()
    ]
    # form.current_farm.choices = [(f.id, f.name) for f in Farmland.query.order_by(Farmland.name).filter(Farmland.harvest_date > dt.date(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day),user_id==user).all()]

    form.phosphorus_unit.choices = [
        (c.id, c.description) for c in Unit.query.order_by(Unit.description).all()
    ]
    form.potassium_unit.choices = [
        (c.id, c.description) for c in Unit.query.order_by(Unit.description).all()
    ]
    form.calcium_unit.choices = [
        (c.id, c.description) for c in Unit.query.order_by(Unit.description).all()
    ]
    if form.validate_on_submit():
        soil = SoilFarmland(
            current_farm_id=form.current_farm.data,
            name=form.name.data,
            soil_date=form.soilsampledate.data,
            soil_depth=form.depth.data,
            soil_organic_level=form.organicmatterlevel.data,
            phosphorus=form.phosphorus.data,
            phosphorus_unit_id=form.phosphorus_unit.data,
            potassium=form.potassium.data,
            potassium_unit_id=form.potassium_unit.data,
            calcium=form.calcium.data,
            calcium_unit_id=form.calcium_unit.data,
            sand=form.sand.data,
            slit=form.slit.data,
            clay=form.clay.data,
            sulfur=form.sulfur.data,
            magnesium=form.magnesium.data,
            boron=form.boron.data,
            copper=form.copper.data,
            zinc=form.zinc.data,
            manganese=form.manganese.data,
        )
        # user_id=user,

        db.session.add(soil)
        db.session.commit()
        flash("A New Soil Test was assigned to a current farmland.", "success")
        return redirect(url_for("main.login"))
    return render_template("soiltest.html", title="Soil Test", form=form)


@main.route("/newfarmland", methods=["GET", "POST"])
@login_required
def insert_farmland_data():
    form = InsertFarmlandForm()
    # user = User.query.get_or_404(current_user.get_id())
    crops = [(c.id, c.description) for c in Crop.query.order_by(Crop.description).all()]
    form.croptype.choices = crops

    if form.validate_on_submit():
        request_data = request.get_json()

        descrip = request_data.get("name")
        crop = int(request_data.get("croptype"))
        coord = (
            request_data.get("coordinates")
            .replace("[", "")
            .replace("]", "")
            .replace("\n", "")
            .replace(" ", "")
        )
        sow = dt.datetime.strptime(request_data.get("sowdate"), "%Y-%m-%d").date()
        harvest = dt.datetime.strptime(
            request_data.get("harvestdate"), "%Y-%m-%d"
        ).date()
        product_expected = float(request_data.get("productexpected"))

        crop = Farmland(
            name=descrip,
            croptype_id=crop,
            sow_date=sow,
            harvest_date=harvest,
            product_expected=product_expected,
            coordinates=coord,
        )
        # user_id=user,

        db.session.add(crop)
        db.session.commit()

        flash("A New Crop Field has been Registered", "success")
        return redirect(url_for("main.login"))
    return render_template("crop.html", title="Insert a New Crop Field", form=form)
