#!/usr/bin/python3
"""
Initialization for the models directory
"""
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage for data storage
storage = FileStorage()

#Reload data from storage (if any) to populate the application
storage.reload()

