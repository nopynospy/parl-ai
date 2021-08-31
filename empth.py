import subprocess

subprocess.run(["parlai interactive -mf zoo:dodecadialogue/empathetic_dialogues_ft/model --inference beam --beam-size 5 --beam-min-length 10 --beam-block-ngram 3 --beam-context-block-ngram 3"])