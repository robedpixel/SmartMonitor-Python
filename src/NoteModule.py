import PIL.Image
import json
from PIL.ExifTags import TAGS

USR_CMT_TAG_ID = 37510


class NoteModule:
    def read_json_from_file(self, url: str) -> [str]:
        raise NotImplementedError()

    def save_notes_to_file(self, url: str, notes: list) -> bool:
        raise NotImplementedError()

    def save_actions_and_notes(self, url: str, actions, notes):
        raise NotImplementedError()


# Stores picture notes in the exif "ImageDescription" tag
class ExifNoteModule(NoteModule):
    def __init__(self):
        NoteModule.__init__(self)

    # read ImageDescription exif tag
    def read_json_from_file(self, url: str):
        img = PIL.Image.open(url)
        exif_data = img.getexif()
        found = False
        if exif_data:
            for tag, value in exif_data.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "UserComment":
                    # Load notes in
                    raw_value = value
                    try:
                        raw_json = json.loads(raw_value)
                        found = True
                        break
                    except KeyError:
                        print("no json stored in UserComment tag")
                        break

                    except ValueError:
                        print("no json stored in UserComment tag")
                        break
        img.close()
        if found:
            return raw_json
        else:
            return None

    def save_notes_to_file(self, url: str, notes: list) -> bool:
        if notes:
            img = PIL.Image.open(url)
            exif_data = img.getexif()
            print("saving notes to exif")
            exif_data[USR_CMT_TAG_ID] = json.dumps(notes, indent=0)
            img.save(url, exif=exif_data)
        else:
            print("no notes to save")
        return True

    def save_actions_and_notes(self, url: str, encoded_actions, notes):
        img = PIL.Image.open(url)
        exif_data = img.getexif()
        json_obj = {}
        if notes:
            print("saving notes to exif")
            json_obj['notes'] = notes
        if encoded_actions:
            json_obj['actions'] = encoded_actions
        exif_data[USR_CMT_TAG_ID] = json.dumps(json_obj, indent=0)
        img.save(url, exif=exif_data)


# Stores picture notes by appending it after the jpg or png image data
class AppendedDataNoteModule(NoteModule):
    NOTE_IDENTIFIER = "@@SmartMonitor@@"

    def read_json_from_file(self, url: str) -> [str]:
        # 1. read data from image
        found = False
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
                    found = True
                except KeyError:
                    print("no json stored in UserComment tag")

                except ValueError:
                    print("no json stored in UserComment tag")
        if found:
            return raw_json
        else:
            return None

    def save_notes_to_file(self, url: str, notes: list) -> bool:
        if notes:
            with open(url, "a+") as f:
                f.write(AppendedDataNoteModule.NOTE_IDENTIFIER)
                f.write(json.dumps(notes, indent=0))
        else:
            print("no notes to save")
        return True

    def save_actions_and_notes(self, url: str, encoded_actions, notes):
        json_obj = {}
        if notes:
            print("saving notes to exif")
            json_obj['notes'] = notes
        if encoded_actions:
            json_obj['actions'] = encoded_actions

        if json_obj:
            with open(url, "a+") as f:
                f.write(AppendedDataNoteModule.NOTE_IDENTIFIER)
                f.write(json.dumps(json_obj, indent=0))
        else:
            print("no notes to save")

        return True
