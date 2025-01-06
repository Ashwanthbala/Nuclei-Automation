import smtplib

with open("reports.txt","r") as file:
    data = file.readlines()


filtered_data = [line.strip() for line in data if '[critical]' in line or '[high]' in line]

extracted_info = []

def sendmail(email,password,msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email,msg)
        server.quit()
        return "Mail Sent Successfully!"
    except:
        return "Error while sending mail!"

for line in filtered_data:
    parts = line.split(' ')
    template = parts[0][1:-1]
    tech_stack = parts[1][1:-1]
    severity = parts[2][1:-1]
    endpoint = parts[3][0:]

    extracted_info.append({
        "Template": template,
        "Tech Stack": tech_stack,
        "Severity": severity,
        "Endpoint": endpoint
    })

formatted_data = "Vulnerability Report\n\n"
for item in extracted_info:
    formatted_data += f"Template: {item['Template']}\n"
    formatted_data += f"Tech Stack: {item['Tech Stack']}\n"
    formatted_data += f"Severity: {item['Severity']}\n"
    formatted_data += f"Endpoint: {item['Endpoint']}\n"
    formatted_data += "-" * 40 + "\n"

print(formatted_data)

mail = sendmail("ashwanthbalajir@gmail.com", "mluu ztsc uatl voag", formatted_data)
print(mail)

