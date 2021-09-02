from parlai.core.params import ParlaiParser
from parlai.core.script import ParlaiScript

class LengthScript(ParlaiScript):

    @classmethod
    def setup_args(cls):
        parser = ParlaiParser(True, True)
        parser.add_argument(
            "--length-filepath",
            type=str,
            help="File to analyze in this script"
        )
        return parser

    def run(self):
        with open(self.opt["length_filepath"]) as f:
            file_content = f.read()
        print(f"Your file has {len(file_content)} characters!")
        return len(file_content)
