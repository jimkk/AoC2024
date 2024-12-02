
"""AoC Helper Functions"""
def read_file(file):
    """Read file and return array of lines"""
    with open(file, 'r', encoding='utf-8') as f:
        data = f.readlines()
    return data
