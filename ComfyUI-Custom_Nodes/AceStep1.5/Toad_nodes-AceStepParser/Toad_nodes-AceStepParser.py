import re

KEY_LIST = [
    "C major", "C# major", "Db major", "D major", "D# major", "Eb major", "E major", "F major", 
    "F# major", "Gb major", "G major", "G# major", "Ab major", "A major", "A# major", "Bb major", "B major",
    "C minor", "C# minor", "Db minor", "D minor", "D# minor", "Eb minor", "E minor", "F minor", 
    "F# minor", "Gb minor", "G minor", "G# minor", "Ab minor", "A minor", "A# minor", "Bb minor", "B minor"
]

SIG_LIST = ["2", "3", "4", "6"]

class AceStepParser:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "master_paste": ("STRING", {"multiline": True, "default": ""}),
                "manual_tags": ("STRING", {"multiline": True, "default": ""}),
                "manual_lyrics": ("STRING", {"multiline": True, "default": ""}),
                "manual_bpm": ("INT", {"default": 0, "min": 0, "max": 300}),
                "manual_duration": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1000.0}),
                # Now using "0" as the first option for quick keyboard resetting
                "manual_keyscale": (["0"] + KEY_LIST,),
                "manual_timesig": (["0"] + SIG_LIST,),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT", "FLOAT", "*", "*")
    RETURN_NAMES = ("tags", "lyrics", "bpm", "duration", "keyscale", "timesignature")
    FUNCTION = "parse_all"
    CATEGORY = "AceStep_Utils"

    def parse_all(self, master_paste, manual_tags, manual_lyrics, manual_bpm, manual_duration, manual_keyscale, manual_timesig):
        # 1. Parse Master Paste
        tags_match = re.search(r"\[tags\]\s*(.*?)\s*\[lyrics\]", master_paste, re.DOTALL | re.IGNORECASE)
        res_tags = tags_match.group(1).strip() if tags_match else ""

        lyrics_match = re.search(r"\[lyrics\]\s*(.*?)\s*Length:", master_paste, re.DOTALL | re.IGNORECASE)
        res_lyrics = lyrics_match.group(1).strip() if lyrics_match else ""

        len_match = re.search(r"Length:\s*([\d\.]+)", master_paste)
        bpm_match = re.search(r"bpm:\s*(\d+)", master_paste)
        key_match = re.search(r"keyscale:\s*([^\r\n]+)", master_paste)
        sig_match = re.search(r"Time Signature:\s*(\d+)", master_paste)

        res_duration = float(len_match.group(1)) if len_match else 0.0
        res_bpm = int(bpm_match.group(1)) if bpm_match else 120
        res_key = key_match.group(1).strip() if key_match else "C major"
        res_sig = sig_match.group(1).strip() if sig_match else "4"

        # 2. Logic: If manual input is empty, "0", or 0.0, use the Paste value
        final_tags = manual_tags if manual_tags.strip() != "" else res_tags
        final_lyrics = manual_lyrics if manual_lyrics.strip() != "" else res_lyrics
        final_bpm = manual_bpm if manual_bpm > 0 else res_bpm
        final_duration = manual_duration if manual_duration > 0.0 else res_duration
        
        # Check if the dropdown is set to the string "0"
        final_key = res_key if manual_keyscale == "0" else manual_keyscale
        final_sig = res_sig if manual_timesig == "0" else manual_timesig

        return (final_tags, final_lyrics, final_bpm, final_duration, final_key, final_sig)

NODE_CLASS_MAPPINGS = {"AceStepParser": AceStepParser}
NODE_DISPLAY_NAME_MAPPINGS = {"AceStepParser": "Toad Nodes: AceStep Song Parser v1.5"}