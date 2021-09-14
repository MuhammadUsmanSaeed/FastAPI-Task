from fastapi import APIRouter
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from starlette.responses import JSONResponse

from schemas.schemas import EmailSchema

conf = ConnectionConfig(
    MAIL_USERNAME="fastapitesting@gmail.com",
    MAIL_PASSWORD="FastAPI@12345",
    MAIL_FROM="fastapitesting@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

router = APIRouter(tags=['Sign up'])

html = """
<p>Thank you for joining us</p> 
"""


@router.post("/email")
async def simple_send(
        email: EmailSchema
) -> JSONResponse:
    message = MessageSchema(
        subject="Welcome To FastAPI",
        recipients=email.dict().get("email"),
        body=html,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
