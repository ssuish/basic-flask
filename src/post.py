from datetime import date

# Get time today
today = date.today()

# Create Dictionary for post
post_list = [
    {
        "Author": "Ssuish",
        "Project": "Flask Web App",
        "Notes": "Sample Text",
        "Date": today.strftime("%B %d, %Y")
    },
    {
        "Author": "Madoka",
        "Project": "Sample Project",
        "Notes": "Sample Text",
        "Date": today.strftime("%B %d, %Y")
    }
]

# Create Title
site_title = {"Home", "About Us", "Projects", "Blogs"}