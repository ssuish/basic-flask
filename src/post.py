# Create Dictionary for post
from datetime import datetime
from xml.etree.ElementTree import tostring


post_list = [
    {
        "Author": "Sssuish",
        "Project": "Flask Web App",
        "Notes": "Sample Text",
        "Date": str(datetime.now)
    },
    {
        "Author": "Madoka",
        "Project": "Sample Project",
        "Notes": "Sample Text",
        "Date": str(datetime.now)
    }
]