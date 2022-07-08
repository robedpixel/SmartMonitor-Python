import PIL.Image
import json
from PIL.ExifTags import TAGS
from collections import deque

IMAGE_DESC_TAG_ID = 270


class NoteModule:
    def __init__(self):
        self.notes = deque()

    def read_notes_from_file(self, url: str) -> [str]:
        raise NotImplementedError()

    def save_notes_to_file(self, url: str) -> bool:
        raise NotImplementedError()


class ExifNoteModule(NoteModule):
    def __init__(self):
        NoteModule.__init__(self)

    # read ImageDescription exif tag
    def read_notes_from_file(self, url: str) -> [str]:
        img = PIL.Image.open(url)
        exif_data = img.getexif()
        if exif_data:
            for tag, value in exif_data.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "ImageDescription":
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
            exif_data[IMAGE_DESC_TAG_ID] = json.dumps(self.notes, indent=0)
            img.save(url, exif=exif_data)
        else:
            print("no notes to save")
        return True


class AppendedDataNoteModule(NoteModule):
    def read_notes_from_file(self, url: str) -> [str]:
        pass
