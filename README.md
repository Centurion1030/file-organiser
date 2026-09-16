#Smart file organiser

A python CLI tool that automatically sorts files in any folder by type and generates an Excel report of all actions. Perfect for cleaning your Downloads, Desktop, or any messy folder in 1 click.

## Features
-**Auto Sorting**: Sorts files into folders:Images, Audio, Documents, Videos,Archives, Code, Others
-**Custom Rules**:Edit 'config.json' to add your own file types and categories
-**Duplicate Handling**: Renames duplicates instead of overwriting. Example: 'video_1230.mp4' 
-**Excel Report**: Creates 'organisation_report.xlsx' with filename, new location, category and timestamp
-**Safe**: Skips folders and the script files themselves

##Tech Stack
'Python 3', 'os', 'shutil', 'pandas', 'openpyxl', 'json'

##Project structure
