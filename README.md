# Google Drive Folder Sync

A simple Python script to sync any local folder with the root of your Google Drive using the PyDrive2 library.

## Features

- Uploads files directly to your Drive root
- Skips files that are already up-to-date
- Updates files if their content has changed
- Works with all common file types

---

## Requirements

- Python 3.x
- `pydrive2`
- Google API credentials (`client_secrets.json`)

---

## Setup Instructions

### 1. Enable the Google Drive API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. In the left menu, go to **"APIs & Services" > "Library"**
4. Search for **"Google Drive API"** and click **Enable**

---

### 2. Create OAuth 2.0 Credentials

1. In the left menu, go to **"APIs & Services" > "Credentials"**
2. Click **"Create Credentials" > "OAuth client ID"**
3. Select **Desktop app** as the application type
4. Download the JSON file after creation
5. Rename the file to `client_secrets.json` and place it in the same folder as `main.py`

---

## Installation

```bash
pip install -r requirements.txt
