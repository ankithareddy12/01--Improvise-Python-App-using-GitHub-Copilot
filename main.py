# Create a Pydantic model for JSON input with a single field "text"
from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

