"""prompts the user for the name of a file and then
outputs that file’s media type according to its suffix"""

type = input("File name: ").strip().lower().rsplit('.')[-1]

match type:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf" | "zip":
        print("application/" + type)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
