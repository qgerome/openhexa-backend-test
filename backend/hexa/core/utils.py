import typing

from django.core.mail import send_mail as django_send_mail
from django.template.loader import render_to_string
from mjml import mjml2html


def send_mail(
    *,
    title: str,
    recipient_list: typing.Sequence[str],
    template_name: str,
    template_variables: typing.Mapping,
):
    text_message = render_to_string(f"{template_name}.txt", template_variables)
    html_message = mjml2html(
        render_to_string(f"{template_name}.mjml", template_variables)
    )

    django_send_mail(
        title,
        message=text_message,
        html_message=html_message,
        recipient_list=recipient_list,
        from_email=None,
    )
