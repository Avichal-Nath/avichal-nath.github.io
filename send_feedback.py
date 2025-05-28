import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, request, render_template

# Flask app
app = Flask(__name__)

# Email configuration
# IMPORTANT: For security reasons, avoid hardcoding sensitive information like passwords directly in your code.
# Consider using environment variables or a more secure configuration management system.
sender_email = "avichalnath314@gmail.com"  # Replace with your email address
# You will need to generate an App Password for your Gmail account if you have 2-Factor Authentication enabled.
# Go to Google Account -> Security -> App Passwords
password = "Yaxcl ssiz lcbs vxjy"  # Replace with your generated App Password

@app.route('/')
def index():
    return render_template('index101.html')

@app.route('/send_feedback', methods=['POST'])
def send_feedback():
    try:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email # Send to yourself
        msg['Subject'] = f"Feedback from {name}: {subject}"

        # Add message body, including the sender's email for reply
        body = f"Name: {name}\nSender Email: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, sender_email, msg.as_string()) # Send from your email to your email

        return "Thank you for your feedback! We'll get back to you as soon as possible"
    except Exception as e:
        # Log the error for debugging
        print(f"Error sending email: {e}")
        return "There was an error sending your feedback. Please try again later.", 500

if __name__ == '__main__':
    # When running locally, ensure you have set up your Gmail App Password
    # and replaced 'YOUR_GENERATED_APP_PASSWORD' above.
    app.run(debug=True)
