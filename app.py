import flask
import psycopg2
import pymysql
from flask import render_template, Flask, request

app = Flask(__name__)
conn = pymysql.connect(host="localhost", user="root", password="", db="mydb")


@app.route("/", methods =["GET","POST"] )
def home1():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        print(password, name)

    return render_template('home.html')






@app.route("/home", methods=["GET","POST"] )
def home():
    if request.method == "POST":
        type = request.form["type"]
        make = request.form["make"]
        registration = request.form["registration"]
        driver = request.form["driver_name"]
        license = request.form["license"]
        year = request.form["year"]
        contact = request.form["contact"]
    # append data into the database

        cursor = conn.cursor()
        sql = "INSERT INTO `details`(`car_type`, `make`, `Vehicle_reg_no`, `driver_name`, `driver_contact`, `year_of_make`, `driver_license_no`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, (type, make, registration,contact,license,year,license))
            conn.commit()  # commit changes to db
            return render_template('capture1.html', msg="Uploaded!")
        except:
            conn.rollback()
            return render_template('capture1.html', msg="Failed!")
    else:
        return render_template('capture1.html')



@app.route("/search", methods =["GET","POST"] )
def search():
    if request.method == "POST":
        qq = 1
        search = request.form["search"]
    #     sql = "SELECT * FROM `details` WHERE 1"
    #     cursor = conn.cursor()
    #     cursor.execute(sql, (search))
    #
    #     # check if cursor has zero rows
    #     if cursor.rowcount == 0:
    #         return render_template('search.html', msg="No such can exists in the database")
    #     else:
    #
    #         rows = cursor.fetchall()
    #         return render_template('search.html', rows=rows)
    #     print(rows)

    #
    # else:
    #     return render_template('search.html')
        sql = "SELECT * FROM `details` WHERE 1"
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            # if row[2]==search:
            """"save the specific row and display it"""
    return render_template('search.html')


@app.route("/renting", methods =["GET","POST"] )
def renting():

    if request.method == "POST":
        name = request.form["name"]
        car = request.form["car"]
        cursor = conn.cursor()
        sql = "INSERT INTO `money`(`Vehicle_reg_no`, `driver`) VALUES (%s, %s)"
        try:
            cursor.execute(sql, (car, name))
            conn.commit()  # commit changes to db
            return render_template('capture1.html', msg="Uploaded!")
        except:
            conn.rollback()
            return render_template('capture1.html', msg="Failed!")
    else:
        return render_template('renting.html')



    return render_template('earnings.html')


@app.route("/money", methods =["GET","POST"] )
def home2():
    if request.method == "POST":
        search = request.form["search"]
        sql = "SELECT * FROM `money` WHERE 1"
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        """search how many times "search" appears in the db call it qq"""
        mulla = """qq*rate"""




    return render_template('earnings.html', msg="you earned {}".format(mulla))



if __name__ == "__main__":
    app.run(debug=True)

