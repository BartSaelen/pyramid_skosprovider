# -*- coding: utf8 -*-

from __future__ import unicode_literals

from skosprovider.providers import (
    DictionaryProvider
)

larch = {
    'id': 1,
    'uri': 'http://python.com/trees/larch',
    'labels': [
        {'type': 'prefLabel', 'language': 'en', 'label': 'The Larch'},
        {'type': 'prefLabel', 'language': 'nl', 'label': 'De Lariks'}
    ],
    'notes': [
        {'type': 'definition', 'language': 'en', 'note': 'A type of tree.'}
    ],
    'matches': {
        'close': ['http://id.python.org/different/types/of/trees/nr/1/the/larch']
    }
}

chestnut = {
    'id': 2,
    'uri': 'http://python.com/trees/chestnut',
    'labels': [
        {'type': 'prefLabel', 'language': 'en', 'label': 'The Chestnut'},
        {'type': 'altLabel', 'language': 'nl', 'label': 'De Paardekastanje'}
    ],
    'notes': [
        {
            'type': 'definition', 'language': 'en',
            'note': 'A different type of tree.'
        }
    ],
    'matches': {
        'related': ['http://id.python.org/different/types/of/trees/nr/17/the/other/chestnut']
    }
}

species = {
    'id': 3,
    'uri': 'http://python.com/trees/species',
    'labels': [
        {'type': 'prefLabel', 'language': 'en', 'label': 'Trees by species'},
        {'type': 'prefLabel', 'language': 'nl', 'label': 'Bomen per soort'}
    ],
    'notes': [
        {
            'type': 'scopeNote', 'language': 'en',
            'note': 'A division of trees.'
        }
    ],    
    'type': 'collection',
    'members': ['1', '2']
}

trees = DictionaryProvider(
    {'id': 'TREES', 'default_language': 'nl'},
    [larch, chestnut, species]
)
