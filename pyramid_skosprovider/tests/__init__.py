# -*- coding: utf8 -*-

from __future__ import unicode_literals

from skosprovider.providers import (
    FlatDictionaryProvider
)

larch = {
    'id': 1,
    'labels': [
        {'type': 'prefLabel', 'language': 'en', 'label': 'The Larch'},
        {'type': 'prefLabel', 'language': 'nl', 'label': 'De Lariks'}
    ],
    'notes': [
        {'type': 'definition', 'language': 'en', 'note': 'A type of tree.'}
    ]
}

chestnut = {
    'id': 2,
    'labels': [
        {'type': 'prefLabel', 'language': 'en', 'label': 'The Chestnut'},
        {'type': 'altLabel', 'language': 'nl', 'label': 'De Paardekastanje'}
    ],
    'notes': [
        {
            'type': 'definition', 'language': 'en',
            'note': 'A different type of tree.'
        }
    ]
}

species = {
    'id': 3,
    'labels': [
        {'type': 'prefLabel', 'language': 'en', 'label': 'Trees by species'},
        {'type': 'prefLabel', 'language': 'nl', 'label': 'Bomen per soort'}
    ],
    'type': 'collection',
    'members': ['1', '2']
}

trees = FlatDictionaryProvider(
    {'id': 'TREES', 'default_language': 'nl'},
    [larch, chestnut, species]
)