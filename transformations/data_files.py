from os.path import splitext


def tsv_to_csv(tsv_file_path):
    with open(tsv_file_path) as tsv_file:
        csv_file_path = splitext(tsv_file_path)[0] + '.csv'
        with open(csv_file_path, 'w') as csv_file:
            for line in tsv_file.readlines():
                csv_file.write(line.replace('\t', ','))
