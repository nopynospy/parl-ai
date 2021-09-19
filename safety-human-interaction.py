from parlai.scripts.interactive import Interactive

"""
Downloads the dialogue safety model.
Allows user to communicate with it in terminal.
Output is saved to a jsonl file.
"""
Interactive.main(
    model_file='zoo:dialogue_safety/single_turn/model',
    model='transformer/classifier',
    print_scores=True,
    single_turn=True,
    outfile='safety-human-emoji.jsonl'
)