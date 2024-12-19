from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def employee_performance():
    # Sample data
    employee = {
        "name": "John Doe",
        "id": "E12345",
        "department": "Engineering",
        "designation": "Software Engineer",
    }
    performance_data = [
        {"project_name": "Project A", "hours": 120, "rating": "Excellent", "remarks": "Great work"},
        {"project_name": "Project B", "hours": 90, "rating": "Good", "remarks": "Needs improvement"},
    ]
    contact_info = "Contact: hr@company.com | Phone: +1 234 567 890"
    return render_template("index.html", employee=employee, performance_data=performance_data, contact_info=contact_info)

if __name__ == "__main__":
    app.run(debug=True)
