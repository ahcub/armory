import csv
from datetime import datetime

from elasticsearch.client import Elasticsearch

es = Elasticsearch()
HOME_DATA = 'home-data'


def delete_index(index_name):
    print(es.indices.delete(index=index_name, ignore=[400, 404]))


def create_record(data):
    print(es.index(index=HOME_DATA, doc_type='data', body=data))


def dump_values_from_file():
    with open(r'C:\Users\Alex\Desktop\indicator_data.csv') as csv_file:
        reader = csv.DictReader(csv_file)

        prev_record = {}
        for row in reader:

            es_data = {key: float(val) for key, val in row.items() if key != 'date'}
            es_data['date'] = datetime.strptime(row['date'], '%d.%m.%Y')
            if prev_record:
                days_passed = (es_data['date'] - prev_record['date']).days
            else:
                days_passed = 1

            diff_dict = {}
            for key, val in es_data.items():
                if key != 'date':
                    diff_dict[key + '_diff'] = (val - prev_record.get(key, val)) / days_passed
            prev_record = es_data

            es_data.update(diff_dict)
            print(es_data)
            create_record(es_data)
            # print(es_data)


if __name__ == '__main__':
    delete_index(HOME_DATA)
    dump_values_from_file()
