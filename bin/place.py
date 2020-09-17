#!/usr/bin/env python
import logging
import json
import argparse
import os

import update
import yaml

# setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)8s %(message)s')
log = logging.getLogger(__name__)


class MicrositeUpdater(update.Updater):
    def place_index_prefix(self, code, lang):
        """ For microsites, the index pages are off the root directory.
        """
        if lang == 'eng':
            return ''
        else:
            return lang

    def place_alternates(self, code, languages):
        if len(languages) == 1:
            return []

        return [{
            'lang': update.LANGUAGES_2[lang],
            'url': '/' if lang == 'eng' else f'/{lang}/',
        } for lang in languages]


def make_muni(code):
    with open("_data/places.json", "r") as f:
        places = json.load(f)

    for place in places:
        if place['code'] == args.place:
            break
    else:
        place_codes = ', '.join([p['code'] for p in places])
        raise ValueError(f"Bad place {args.place}, must be one of: {place_codes}")

    updater = MicrositeUpdater()
    updater.skip_archive = args.quick
    updater.skip_images = args.quick
    updater.update_content([args.place])

    # update _data/place.json
    with open("_data/place.json", "w") as f:
        json.dump(place, f, indent=2, sort_keys=True)

    # update the base URL in _config.yml
    with open("_config.yml", "r") as f:
        info = yaml.safe_load(f)

    with open("_config.yml", "w") as f:
        info['url'] = 'https://' + place['bucket']
        yaml.dump(info, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('place', help='Place code to generate the website for')
    parser.add_argument('--quick', action='store_true', default=False)
    args = parser.parse_args()

    make_muni(args)
