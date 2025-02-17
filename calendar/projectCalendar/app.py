from flask import Flask, render_template
import calendar

app = Flask(__name__)

@app.route("/")
def index():
    # Создаём календарь
    cal = calendar.TextCalendar()
    calendar_output = cal.formatyear(2025, 2, 1, 6, 3)
    
    # Передаём календарь в шаблон
    return render_template("index.html", calendar_output=calendar_output)

if __name__ == "__main__":
    app.run(debug=True)
