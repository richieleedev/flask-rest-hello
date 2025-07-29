import os
import sys
from sqlalchemy import MetaData
from eralchemy2 import render_er
from src.models import db
from sqlalchemy.orm import DeclarativeMeta

# This file assumes you are inside the Flask shell or have access to the metadata
metadata = db.metadata  

# Output diagram
output_file = "diagram.png"

if __name__ == "__main__":
    render_er(metadata, output_file)
    print(f"ER diagram saved to {output_file}")
