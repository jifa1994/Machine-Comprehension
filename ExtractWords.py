import json


path = "./train-v2.0.json"

json_file = open(path, 'r', encoding='utf-8')
file = json.load(json_file)

def write_train_data(path, file):
    dump = []
    for paragraphs in file['data']:
        for paragraph in paragraphs['paragraphs']:
            if 'qas' in paragraph:
                context = paragraph['context']
                for qa in paragraph['qas']:
                    question = qa['question']
                    qid = qa['id']
                    is_impossible = qa['is_impossible']
                    if is_impossible:
                        answer_start = 0
                        answer_end = answer_start + len(context)
                        text = ''
                        dump.append(dict([('qid', qid),
                                          ('context', context),
                                          ('question', question),
                                          ('text', text),
                                          ('answer_start', answer_start),
                                          ('answer_end', answer_end)]))
                    answers = qa['answers'] if 'answers' in qa else []
                    for answer in answers:
                        text = answer['text']
                        answer_start = answer['answer_start']
                        answer_end = answer_start + len(text)
                        dump.append(dict([('qid', qid),
                                              ('context', context),
                                              ('question', question),
                                              ('text', text),
                                              ('answer_start', answer_start),
                                              ('answer_end', answer_end)]))
    with open(path, 'w', encoding='utf-8') as f:
        for line in dump:
            json.dump(line, f)
            print('', file=f)


write_train_data('dump.json', file)
