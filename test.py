import parlai
from parlai.scripts.interactive import interactive
# from parlai.core.build_data import modelzoo_path
from parlai.core.params import ParlaiParser
from parlai.core.agents import Agent
from parlai.core.opt import Opt
from parlai.core.worlds import create_task
from parlai.core.build_data import modelzoo_path
import os

# print(modelzoo_path('','zoo:dodecadialogue/empathetic_dialogues_ft/model'))

parser = ParlaiParser(add_model_args=True)
# parser.parse_and_process_known_args('zoo:dodecadialogue/empathetic_dialogues_ft/model')
# parser.opt["model-file"]
# print(parser)

model_dict = {
#   'zoo': 'dodecadialogue/empathetic_dialogues_ft/model',
  'model_file': 'zoo:dodecadialogue/empathetic_dialogues_ft/model',
  'inference': 'beam',
  'beam_size': 5,
  'beam-min-length': 10,
  'beam-block-ngram': 3,
  'beam-context-block-ngram': 3,
  'datapath':  os.path.dirname(parlai.__file__),
  'n_image_tokens': 1,
  'n_image_channels': 1,
  'image_fusion_type': 'late'
}

opt = Opt(model_dict)
print(opt)

interactive(opt)