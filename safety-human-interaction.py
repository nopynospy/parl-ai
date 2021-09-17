from parlai.scripts.interactive import Interactive

Interactive.main(
    model_file='zoo:dialogue_safety/single_turn/model',
    model='transformer/classifier',
    print_scores=True,
    single_turn=True,
    outfile='safety-human-emoji.jsonl'
)