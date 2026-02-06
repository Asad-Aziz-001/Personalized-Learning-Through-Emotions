# test_email.py
import smtplib
from email.mime.text import MIMEText

# --- UPDATE THESE ---
EMAIL = "lianaedwin234@gmail.com"
PASSWORD = "wswanstfoabzvqyd" # NO SPACES!
# ---------------------

msg = MIMEText("If you see this, your email configuration is correct!")
msg['Subject'] = "Test Email from Sentellect"
msg['From'] = EMAIL
msg['To'] = EMAIL

try:
    print("Connecting to Gmail...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    print("Logging in...")
    server.login(EMAIL, PASSWORD)
    
    print("Sending email...")
    server.send_message(msg)
    
    print("✅ SUCCESS! Email sent. Your credentials work.")
    server.quit()
except Exception as e:
    print("\n❌ ERROR:", e)
    print("\nPossible causes:")
    print("1. You used your login password instead of an App Password.")
    print("2. You included spaces in the App Password.")
    print("3. 2-Step Verification is not enabled on your Google Account.")