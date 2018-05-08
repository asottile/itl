import argparse
import datetime
import os.path
import xml.sax.handler


FROM_VALUE = {
    'integer': int,
    'string': lambda s: s,
    'date': lambda s: datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ'),
}


class Handler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.songs = []
        self._in_key = False
        self._in_value = None
        self._attr = None
        self._in_dict = 0
        self._in_array = 0

    def characters(self, content):
        if self._in_key:
            self._attr = content
            self._in_key = False
        elif self._in_value:
            self.songs[-1][self._attr] = FROM_VALUE[self._in_value](content)
            self._in_value = None
            self._attr = None

    def startElement(self, name, attrs):
        if name == 'dict':
            self._in_dict += 1
        elif name == 'array':
            self._in_array += 1
        elif self._in_array:
            return
        elif name == 'key' and self._in_dict == 2:
            self.songs.append({})
        elif name == 'key' and self._in_dict == 3:
            self._in_key = True
        elif name in {'integer', 'date', 'string'} and self._in_dict == 3:
            self._in_value = name

    def endElement(self, name):
        if name == 'dict':
            self._in_dict -= 1
        elif name == 'array':
            self._in_array -= 1


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--library-xml',
        # TODO: is this true on windows?
        default=os.path.expanduser('~/Music/iTunes/iTunes Music Library.xml'),
    )
    args = parser.parse_args(argv)

    handler = Handler()
    with open(args.library_xml) as f:
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.setFeature(xml.sax.handler.feature_external_ges, False)
        parser.parse(f)


if __name__ == '__main__':
    exit(main())
