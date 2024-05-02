from flask import Flask, render_template, send_from_directory,request
import smtplib

MY_EMAIL = "saadmulla91@gmail.com"
PASSWORD = "qyydhsbwlmruomel"

app = Flask(__name__)

def send_mail(name, email, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  
        connection.starttls()  
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:New Message\n\nName:{name}\nEmail:{email}\nMessage:{message}")

#Home page
@app.route('/')
def home():
    return render_template('index.html')

#Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

#Skill & Certificate page
@app.route('/skill_certification')
def skill_certification():
    return render_template('skill_certification.html')

@app.route('/download')
def download():
    return send_from_directory('static', path='files/cv resume.pdf')

@app.route('/sendemail', methods=['POST'])
def sendemail():
    name = request.form['name']
    email = request.form['email_box']
    message = request.form['text_box']
    send_mail(name=name, email=email, message=message)
    return render_template('/email_send.html')

if __name__ == "__main__":
    app.run(debug=False)
    