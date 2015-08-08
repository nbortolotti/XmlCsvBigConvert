__author__ = 'nbortolotti'

import csv
import cStringIO
from lxml import etree

class xmlcsv:
    def __init__(self, input_file, output_file, row, schema):
        xml_file = open(input_file, "r")
        col = schema
        resultado = []
        for _, element in etree.iterparse(xml_file, tag=row):
            rows = list(element.iter('row'))
            for row_element in rows:
                row_tmp = []
                a = 0
                while a < len(col):
                    row_tmp.insert(a, row_element.get(col[a]))
                    #print (row_element.get(col[a]))
                    a += 1
                resultado.append(dict(zip(col, row_tmp)))

        test_file = open(output_file, 'wb')
        writer = UnicodeDictWriter(test_file, col)
        writer.writerows(resultado)
        test_file.close()

class UnicodeWriter(object):

    def __init__(self, f, dialect=csv.excel_tab, encoding="utf-16", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoding = encoding

    def writerow(self, row):
        # Modified from original: now using unicode(s) to deal with e.g. ints
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = data.encode(self.encoding)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

class UnicodeDictWriter(UnicodeWriter):

    def __init__(self, f, fields, dialect=csv.excel,
                 encoding="utf-8", **kwds):
        super(UnicodeDictWriter, self).__init__(f, dialect, encoding, **kwds)
        self.fields = fields

    def writerow(self, drow):
        row = [drow.get(field, '') for field in self.fields]
        super(UnicodeDictWriter, self).writerow(row)
