def send_mail(subject, body, recipient):
    from_email = 'noreply@example.com'
    message = f'Subject: {subject}\n\n{body}'
    send_mail(subject, message, from_email, [recipient])
