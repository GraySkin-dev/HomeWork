import os


FILES_LIST = ['1.txt', '2.txt', '3.txt']
OUTPUT_FILE = 'output.txt'


def get_from_file(file_name):
    f = os.path.join('files', file_name)
    with open(f, 'r', encoding='UTF-8') as file:
        file_lines = file.readlines()
    file_lines.insert(0, str(len(file_lines)) + '\n')
    file_lines.insert(0, file_name + '\n')
    return file_lines

def write_to_file(file_name, files_lines):
    f = os.path.join('files', file_name)
    with open(f, 'w', encoding='UTF-8') as file:
        for file_lines in files_lines:
            file_lines[-1] = file_lines[-1].strip('\n')
            file.writelines(file_lines)
            file.write('\n')

def sort_by_length(files_list):
    files_lines = []
    x = 0
    while x < len(files_list):
        file_lines = get_from_file(files_list[x])
        files_lines += [file_lines]
        x += 1
    files_lines.sort(key=len)
    return files_lines


write_to_file(OUTPUT_FILE, sort_by_length(FILES_LIST))