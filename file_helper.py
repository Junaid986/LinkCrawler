import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory {}'.format(directory))
        os.mkdir(directory)

def create_data_files(name, base_url, queuefile, crawlfile):
    if not os.path.exists(queuefile):
        write_file(queuefile, base_url)
    if not os.path.exists(crawlfile):
        write_file(crawlfile, '')

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_to_file(file, data):
    f = open(file, 'a')
    f.write(data + '\n')

def delete_file_content(file):
    with open(file, 'w'):
        pass

def file_to_set(file):
    results = set();
    with open(file,'r') as f:
        for line in f:
            results.add(line.replace('\n',' '))
    return results

def set_to_file(set, file):
    delete_file_content(file)
    for link in set:
        append_to_file(file, link)

