

import os
import shutil
import sys


def main():
    """
    scan files in Download and sort it out
    
    """


    out = program_main_logic()
    print(out)




def program_main_logic():
    
    checker = operating_system_checker()

    header = f"*"*10 + " FILES SORTING HANDLER " + "*"*10

    message = input(
        f"\n{header}\n"
        "1: scan files \n"
        "2: Sort files in Download folder\n"
        "\nselect option to continue or 'n' to exit program: \n"
    ).strip().lower()


    match message:
        case "n":
            sys.exit()
        case "1":
            return file_folder_scanner()
        case "2":
            return sorting_operations_Downloads()
        case _:
            return "invalid user choice! "



def file_folder_scanner():

    messge = input (
        "\nselect the ROOT folder you want to scan it's content\n"
        "1: Documents\n"
        "2: Downloads \n"
        "3: Videos\n"
        "4: Pictures\n"
    )

    match messge:
        case "1":
            path = os.path.expanduser("~/Documents")
            scan = os.listdir(path)
            for file in scan:
                print(file)
        case "2":
            path = os.path.expanduser("~/Downloads")
            scan = os.listdir(path)
            for file in scan:
                print(file)
        case "3":
            path = os.path.expanduser("~/Videos")
            scan = os.listdir(path)
            for file in scan:
                print(file)
        case "4":
            path = os.path.expanduser("~/Pictures")
            scan = os.listdir(path)
            for file in scan:
                print(file)
        case _:
            return "invalid user choice"









def operating_system_checker():

    check = sys.platform
    if check == "linux":
        return "Computer is a Debian OS(Ubuntu)"
    
    elif check == "win32":
        return "Computer is Windows"

    elif check =="darwin":
        return "computer is a MacOS"
    
    return check







    
def file_sorter():

    root_downloads_folder = os.path.expanduser("~/Downloads")
    path = os.listdir(root_downloads_folder)

    
    try:
        if "MOVIE_FILES" not in path:
            movie = os.mkdir(f"{root_downloads_folder}/MOVIES_FILES")
        else:
            return "movie folder exist"
            
        if "MUSIC_FILES" not in path:
            music = os.mkdir(f"{root_downloads_folder}/MUSIC_FILES")
        else:
            return "music folder found"
        
        if "DOCUMENT_FILES" not in path:
            document = os.mkdir(f"{root_downloads_folder}/DOCUMENT_FILES")
        else:
            return "document folder found"
        if "SOFTWARE_FILES" not in path:
            software = os.mkdir(f"{root_downloads_folder}/SOFTWARE_FILES")
        else:   
            return "software  folder found "
        if "PICTURE_FILES" not in path:
            picture = os.mkdir(f"{root_downloads_folder}/PICTURE_FILES")
            
    except (FileExistsError):
        return "file exist"
    
    return movie ,music, document, software,picture, root_downloads_folder








def sorting_operations_Downloads():

    file_sorter()

    
    
    path = os.path.expanduser("~/Downloads")
    downloads  =os.listdir(path)
    # print(downloads)

    for file in downloads:
            if file.endswith((".mkv", ".mp4", ".avi", ".mov", ".wmv", ".flv", ".webm")):
                # print(file, "Moved Successfully")
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"/home/localcode-tech/Downloads/MOVIES_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)
            elif file.endswith((".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a")):
                # print(file, "Moved Successfully")
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"/home/localcode-tech/Downloads/MUSIC_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)

            elif  file.endswith((".zip", ".iso", ".msi", ".dmg", ".exe", ".rar", "7z")):
                # print(file, "Moved Successfully")
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"/home/localcode-tech/Downloads/SOFTWARE_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)
            elif file.endswith((".pdf", ".txt", ".csv", ".docx", ".xlsx", ".pptx", ".odt")):
                # print(file, "move successfully")
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"/home/localcode-tech/Downloads/DOCUMENT_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)
            elif file.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", "webp", ".tiff", ".svg")):
                try:
                    shutil.move(src=f"{path}/{file}", dst=f"/home/localcode-tech/Downloads/DOCUMENT_FILES")
                except (FileExistsError, FileNotFoundError) as e:
                    print(e)

    return "Files Movies Successfully"


    

     
    

if __name__== "__main__":
    main()