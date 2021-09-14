# from celery import Celery
# from celery.utils.log import get_task_logger
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
# from starlette.responses import JSONResponse
#
# # Initialize celery
# celery = Celery('tasks', broker='amqp://guest:guest@127.0.0.1:5672//')
# # Create logger - enable to display messages on task logger
# celery_log = get_task_logger(__name__)
#
# conf = ConnectionConfig(
#     MAIL_USERNAME="fastapitesting@gmail.com",
#     MAIL_PASSWORD="FastAPI@12345",
#     MAIL_FROM="fastapitesting@gmail.com",
#     MAIL_PORT=587,
#     MAIL_SERVER="smtp.gmail.com",
#     MAIL_TLS=True,
#     MAIL_SSL=False,
#     USE_CREDENTIALS=True,
#     VALIDATE_CERTS=True
# )
#
# html = """
# <p>Thank you for joining us</p>
# """
#
#
# @celery.task(name="send_email")
# def add_email(current_email):
#     print(current_email)
#     send_simple_email(current_email)
#     celery_log.info(f"Email Send!")
#
#
# async def send_simple_email(current_email) -> JSONResponse:
#     message = MessageSchema(
#         subject="Welcome To FastAPI",
#         recipients=current_email,
#         body=html,
#         subtype="html"
#     )
#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return JSONResponse(status_code=200, content={"message": "email has been sent"})
