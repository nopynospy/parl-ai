# parl-ai

# Run Emphathic Model
parlai interactive -mf zoo:dodecadialogue/empathetic_dialogues_ft/model --inference beam --beam-size 5 --beam-min-length 10 --beam-block-ngram 3 --beam-context-block-ngram 3

# Common fixes

1. EOFError: Compressed file ended before the end-of-stream marker was reached
- Delete all files in emphathetic_dialogues_ft

# To-do
1. Fix RuntimeError: No task specified. Please select a task with --task {task_name}.