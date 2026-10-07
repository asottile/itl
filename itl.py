import argparse
import collections
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


def get_songs(filename):
    handler = Handler()
    with open(filename) as f:
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.setFeature(xml.sax.handler.feature_external_ges, False)
        parser.parse(f)
    return handler.songs


def _ngettext(n, s, p):
    if n == 1:
        return s.format(n=n)
    else:
        return p.format(n=n)


def human_time(rest):
    days, rest = divmod(rest, 60 * 60 * 24)
    hours, rest = divmod(rest, 60 * 60)
    minutes, seconds = divmod(rest, 60)
    ret = []
    if days:
        ret.append(_ngettext(days, '{n} Day', '{n} Days'))
    if hours:
        ret.append(_ngettext(hours, '{n} Hour', '{n} Hours'))
    if minutes:
        ret.append(_ngettext(minutes, '{n} Minute', '{n} Minutes'))
    if seconds:
        ret.append(_ngettext(seconds, '{n} Second', '{n} Seconds'))
    return ', '.join(ret)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--library-xml',
        default=os.path.expanduser('~/Music/iTunes/iTunes Music Library.xml'),
    )
    args = parser.parse_args(argv)

    time_by_artist = collections.Counter()
    time_by_song = collections.Counter()
    plays_by_song = collections.Counter()
    for song in get_songs(args.library_xml):
        song_count = song.get('Play Count', 0)
        song_time = song['Total Time'] * song_count // 1000
        time_by_artist[song['Artist']] += song_time
        time_by_song[(song['Artist'], song['Name'])] += song_time
        plays_by_song[(song['Artist'], song['Name'])] += song_count

    print('=' * 79)
    print(f'Total listening time: {human_time(sum(time_by_artist.values()))}')

    print('=' * 79)
    print('Top artists (by play time)')
    print('=' * 79)
    for i, (artist, t) in enumerate(time_by_artist.most_common(10), 1):
        print(f'{i}. {artist}: {human_time(t)}')

    print('=' * 79)
    print('Top songs (by count)')
    print('=' * 79)
    for i, ((artist, song), n) in enumerate(plays_by_song.most_common(25), 1):
        print(f'{i}. [{artist}] {song}: {n}')

    print('=' * 79)
    print('Top songs (by play time)')
    print('=' * 79)
    for i, ((artist, song), t) in enumerate(time_by_song.most_common(25), 1):
        print(f'{i}. [{artist}] {song}: {human_time(t)}')


if __name__ == '__main__':
    raise SystemExit(main())
