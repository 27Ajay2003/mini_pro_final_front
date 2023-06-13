from drf_yasg import openapi

title = "Your API Title"
version = "1.0.0"

contact = openapi.Contact(email="your-email@example.com")

swagger_info = openapi.Info(
    title=title,
    default_version=version,
    contact=contact,
)
