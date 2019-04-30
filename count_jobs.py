import json
import os

class IndeedAPIHelper(object):
    def __init__(self):
        location = 'Chicago, IL'
        engineer_job_titles = ['process', 'software', 'chemical', 'biomedical']
    def build_query(self):
        pass

def get_count_from_results(job_data):
    job_count = job_data['totalResults']
    return job_count

def load_json_results(query_path_result):
    with open(query_path_result, 'r') as f:
        job_data = json.load(f, strict=False)
    return job_data

def main():
    # TODO - in the real version, use the Indeed API helper to get queries to save to files
    # TODO - (or a single file (load would need to be redone in this instance))
    query_folder  = 'query_results'
    # TODO - save count to file? print it?
    total_count = 0
    for query_fn in os.listdir(query_folder):
        query_result_path = os.path.join(query_folder, query_fn)
        job_data = load_json_results(query_result_path)
        total_count += get_count_from_results(job_data)
    print('There are {} engineering positions in Chicago'.format(total_count))

if __name__ == '__main__':
    main()
