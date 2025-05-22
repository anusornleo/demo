from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings

def send_confirmation_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    confirm_url = f"http://localhost:3000/confirm-email/?uid={uid}&token={token}"
    send_mail(
        subject="Confirm your email",
        message=f"Click to confirm: {confirm_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )

def send_password_reset_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    url = f"http://localhost:3000/reset-password/?uid={uid}&token={token}"
    send_mail("Reset your password", f"Reset here: {url}", settings.DEFAULT_FROM_EMAIL, [user.email])
