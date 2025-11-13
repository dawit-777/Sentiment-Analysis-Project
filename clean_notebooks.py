import nbformat, glob

for f in glob.glob("*.ipynb"):  # or use "**/*.ipynb" for subfolders
    nb = nbformat.read(f, as_version=4)
    for cell in nb.cells:
        if 'metadata' in cell and 'widgets' in cell['metadata']:
            del cell['metadata']['widgets']
    nbformat.write(nb, f)
    print(f"Fixed {f}")
