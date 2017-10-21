import os
import csv
import datetime


class Exporter(object):
    def __init__(self):
        self.writableDirPath = './results'
        if not os.path.isdir(self.writableDirPath):
            os.makedirs(self.writableDirPath)

    def exportToCSV(self, win_loss):
        filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv'
        with open(os.path.join(self.writableDirPath, filename), 'wt') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for line in win_loss:
                writer.writerow(line)

        print('Exported as ' + filename)
