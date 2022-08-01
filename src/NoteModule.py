import PIL.Image
import json
from PIL.ExifTags import TAGS

USR_CMT_TAG_ID = 37510


class NoteModule:
    def __init__(self):
        self.notes = []

    def read_notes_from_file(self, url: str) -> [str]:
        raise NotImplementedError()

    def save_notes_to_file(self, url: str) -> bool:
        raise NotImplementedError()


# Stores picture notes in the exif "ImageDescription" tag
class ExifNoteModule(NoteModule):
    def __init__(self):
        NoteModule.__init__(self)

    # read ImageDescription exif tag
    def read_notes_from_file(self, url: str):

        img = PIL.Image.open(url)
        exif_data = img.getexif()
        if exif_data:
            for tag, value in exif_data.items():
                decoded = TAGS.get(tag, tag)
                print(tag)
                if decoded == "UserComment":
                    # Load notes in
                    raw_value = value
                    try:
                        raw_json = json.loads(raw_value)
                        if isinstance(raw_json, list):
                            self.notes = raw_json
                        else:
                            print("no notes found for jpg")
                    except ValueError:
                        print("no notes found for jpg")
        pass

    def save_notes_to_file(self, url: str) -> bool:
        if self.notes:
            img = PIL.Image.open(url)
            exif_data = img.getexif()
            print("saving notes to exif")
            exif_data[USR_CMT_TAG_ID] = json.dumps(self.notes, indent=0)
            img.save(url, exif=exif_data)
        else:
            print("no notes to save")
        return True


# Stores picture notes by appending it after the jpg or png image data
class AppendedDataNoteModule(NoteModule):
    NOTE_IDENTIFIER = "@@SmartMonitor@@"

    def read_notes_from_file(self, url: str) -> [str]:
        # 1. read data from image
        with open(url, 'rb') as f:
            img_data = f.read()
            # 2. get end of image
            result = img_data.split(AppendedDataNoteModule.NOTE_IDENTIFIER.encode())
            # 3. read data after image
            if len(result) > 1:
            # 4. check if valid json
            # 5. if valid, load in
                try:
                    raw_json = json.loads(result[1])
                    if isinstance(raw_json, list):
                        self.notes = raw_json
                    else:
                        print("no notes found for jpg")
                except ValueError:
                    print("no notes found for jpg")
        pass

    def save_notes_to_file(self, url: str) -> bool:
        if self.notes:
            with open(url, "a+") as f:
                f.write(AppendedDataNoteModule.NOTE_IDENTIFIER)
                f.write(json.dumps(self.notes, indent=0))
        else:
            print("no notes to save")
        return True
