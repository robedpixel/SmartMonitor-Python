import PIL.Image
from PIL.ExifTags import TAGS

IMAGE_DESC_TAG_ID = 270


class NoteModule:
    def __init__(self):
        self.notes = list()

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
                    self.notes = value
        pass

    def save_notes_to_file(self, url: str) -> bool:
        if self.notes:
            img = PIL.Image.open(url)
            exif_data = img.getexif()
            print("saving notes to exif")
            exif_data[IMAGE_DESC_TAG_ID] = self.notes
            img.save(url, exif=exif_data)
        else:
            print("no notes to save")
        return True


class AppendedDataNoteModule(NoteModule):
    def read_notes_from_file(self, url: str) -> [str]:
        pass
