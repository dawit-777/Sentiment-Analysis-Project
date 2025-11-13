import nbformat, glob

# Recursively find all notebooks in current folder and subfolders
for f in glob.glob("**/*.ipynb", recursive=True):
    nb = nbformat.read(f, as_version=4)
    changed = False
    for cell in nb.cells:
        if 'metadata' in cell and 'widgets' in cell['metadata']:
            del cell['metadata']['widgets']
            changed = True
    if changed:
        nbformat.write(nb, f)
        print(f"Fixed {f}")
    else:
        print(f"No fix needed for {f}")
