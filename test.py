from parlai.scripts.interactive import interactive
# from parlai.core.build_data import modelzoo_path
from parlai.core.params import ParlaiParser
from parlai.core.agents import Agent
from parlai.core.worlds import create_task

# print(modelzoo_path('','zoo:dodecadialogue/empathetic_dialogues_ft/model'))

parser = ParlaiParser(add_model_args=True)
parser.parse_and_process_known_args('zoo:dodecadialogue/empathetic_dialogues_ft/model')

interactive(parser)