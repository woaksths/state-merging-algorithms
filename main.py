from algorithm import *
from FAdo.reex import str2regexp

if __name__ == '__main__':

    data_path = 'data/total/max_set20/set2regex/test.txt'

    with open(data_path, 'r') as rf:
        test_data = rf.read().split('\n')
        match = 0
        for data in test_data:
            ground_truth = data.split('\t')[-1].replace(' ','')
            ground_truth = preprocess_regex(ground_truth)
            data = data.split('\t')[:-1]
            data = list(filter(('none').__ne__, data))
            data = [d.replace(' ','') for d in data]
            prediction_regex = synthesize(data).toDFA()
            regexp = str2regexp(ground_truth).toDFA()

            if regexp.equal(prediction_regex):
                print('input: ', data)
                print('ground truth: ', regexp.reCG())
                print('prediction : ', prediction_regex.reCG())
                print('\n')
                match+=1

        accuracy = float(match / len(test_data))
        print('Accuracy: ', accuracy)
