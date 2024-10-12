from flask import Flask, request, jsonify, render_template, redirect, url_for
import mysql.connector as connector
from utills import check_data_validation

app = Flask(__name__)

# Connect to the MySQL database
mydb = connector.connect(
    host="localhost",
    user="neetu",
    password="Neetu#1234",
    database="Student_db"
)

# Route to render the HTML form
@app.route("/form", methods=["GET"])
def render_form():
    return render_template("add_student.html")  

# Route to handle form submission and store data in the database
@app.route("/add_student", methods=["POST"])
def add_student():
    student_id= request.form.get('student_id')
    full_name = request.form.get('full_name')
    father_name = request.form.get('father_name')
    mother_name = request.form.get('mother_name')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    house = request.form.get('house')
    class_ = request.form.get('class')
    section = request.form.get('section')
    phone_no = request.form.get('phone_no')

    status =True
    message ="working on it"
    # message, status = check_data_validation(full_name,father_name,mother_name)
    if status:
        cursor = mydb.cursor()
        query = """
            INSERT INTO student ( stuid ,full_name, father_name, mother_name, dob, gender, house, classes, section, phone_no)
            VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)
        """
        values = (student_id,full_name, father_name, mother_name, dob, gender, house, class_, section, phone_no)
        try:
            cursor.execute(query, values)
            mydb.commit()
            return redirect(url_for('home.html'))  
        except connector.Error as err:
            return jsonify({"error": str(err)}), 500
        finally:
            cursor.close()
    else:
        return jsonify({"message": message}), 400

if __name__ == "__main__":
    app.run(debug=True)
