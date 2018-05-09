import argparse
import datetime
import os.path
import xml.sax.handler


CONV = {
    'integer': int,
    'string': lambda s: s,
    'date': lambda s: datetime.datetime.strptime(s, '%Y-%m-%dT%H:%M:%SZ'),
    'true': lambda _: True,
    'false': lambda _: False,
}


class Handler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.songs = []
        self._depths = {'array': 0, 'dict': 0}
        self._in_key, self._in_val = False, False
        self._key, self._val = '', ''

    def characters(self, content):
        if self._in_key:
            self._key += content
        elif self._in_val:
            self._val += content

    def startElement(self, name, _):
        if name in self._depths:
            self._depths[name] += 1
        elif self._depths['array']:
            return
        elif name == 'key' and self._depths['dict'] == 2:
            self.songs.append({})
        elif name == 'key' and self._depths['dict'] == 3:
            self._in_key = True
        elif name in CONV and self._depths['dict'] == 3:
            self._in_val = True

    def endElement(self, name):
        if name in self._depths:
            self._depths[name] -= 1
        elif self._in_key:
            self._in_key = False
        elif self._in_val:
            self._in_val = False
            self.songs[-1][self._key] = CONV[name](self._val)
            self._key, self._val = '', ''


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--library-xml',
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
