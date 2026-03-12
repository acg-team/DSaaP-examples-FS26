# bad:
def analyse_users(users):
    print("Starting analysis...")
    for u in users:
        if u.age > 18:
            send_email(u.email)


# better:
def notify_users(users):
    log_start()
    email_adult_users(users)