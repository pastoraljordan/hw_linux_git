from app import myapp_obj

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myapp_obj.route("/")
def home():
    return render_template('home.html', name = name, city_names = city_names)
