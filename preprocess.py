import os


def create_metadata(dataset_dir, out='metadata'):
    composer_map = {}
    for root, subdirs, files in os.walk(dataset_dir):
        composer = root.split('/')[-1]
        for file in files:
            if composer in composer_map:
                composer_map[composer].append(file)
            else:
                composer_map[composer] = [file]

    if not os.path.isdir(out):
        os.mkdir(out)

    with open(os.path.join(out, 'composer_map.tsv'), 'w') as writer:
        for composer, files in composer_map.items():
            for file in files:
                writer.write('{0}    {1}'.format(composer, file))


if __name__ == '__main__':
    create_metadata('/home/snowman/Documents/datasets/piano_midi')
