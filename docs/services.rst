.. _services:

=====================
Service Documentation
=====================

This library takes your skosproviders and makes them available as REST services. 
The pyramid_skosprovider serves JSON  as a REST service so it can be used easily inside a AJAX webbrowser call or by an external program.

The following API is present:

.. http:get:: /conceptschemes
    
    Get all registered conceptschemes.
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes HTTP/1.1
        Host: localhost:6543
        Accept: application/json
    
    **Example response**:
    
    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type:  application/json; charset=UTF-8
        Date:  Mon, 14 Apr 2014 14:42:34 GMT

        [
            {
                "id": "TREES",
                "uri": "urn:x-skosprovider:trees",
                "label": "Different types of trees."
            }
        ]


    :statuscode 200: The list of conceptschemes was found.

   
.. http:get:: /conceptschemes/{scheme_id}
    
    Get information about a concept scheme.
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes/TREES
        Host: localhost:6543
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Length:  15
        Content-Type:  application/json; charset=UTF-8
        Date:  Mon, 14 Apr 2014 14:45:37 GMT
        Server:  waitress

        {
            "id": "TREES",
            "uri": "urn:x-skosprovider:trees",
            "label": "Different types of trees.",
            "labels": [
                {"type": "prefLabel", "language": "en", "label": "Different types of trees."},
                {"type": "prefLabel", "language": "nl", "label": "Verschillende soorten bomen."}
            ]
        }

    **Example request**:
    
    -.. sourcecode:: http
    
        GET /conceptschemes/PLANTS
        Host: localhost:6543
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 404 Not Found
        Content-Length:  775
        Content-Type:  text/html; charset=UTF-8
        Date:  Tue, 15 Apr 2014 20:32:52 GMT
        Server:  waitress

    :statuscode 200: The conceptscheme was found.
    :statuscode 404: The conceptscheme was not found.

.. http:get:: /conceptschemes/{scheme_id}/topconcepts
    
    Get all top concepts in a certain conceptscheme. These are all the concepts
    in the conceptscheme that have no broader concept.
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes/TREES/topconcepts
        Host: localhost:6543
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type:  application/json; charset=UTF-8
        Date:  Mon, 14 Apr 2014 14:47:33 GMT
        Server:  waitress

        [
            {
                "id": "1", 
                "uri": "urn:x-skosprovider:TREES:1",
                "type": "concept",
                "label": "De Lariks"
            }, {
                "id": "2", 
                "uri": "urn:x-skosprovider:TREES:2",
                "type": "concept",
                "label": "De Paardekastanje"
            }
        ]

    :statuscode 200: The topconcepts in this conceptscheme were found.
    :statuscode 404: The conceptscheme was not found.

.. http:get:: /conceptschemes/{scheme_id}/displaytop
    
    Get the top of a display hierarchy. Depending on the underlying provider
    this will be a list of Concepts and Collections.

    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes/TREES/displaytop
        Host: localhost:6543
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type:  application/json; charset=UTF-8
        Date:  Mon, 14 Apr 2014 14:47:33 GMT
        Server:  waitress

        [
            {
                "id": "1", 
                "uri": "urn:x-skosprovider:TREES:1",
                "type": "concept",
                "label": "De Lariks"
            }, {
                "id": "2", 
                "uri": "urn:x-skosprovider:TREES:2",
                "type": "concept",
                "label": "De Paardekastanje"
            }
        ]

    :statuscode 200: The concepts and collections were found.
    :statuscode 404: The conceptscheme was not found.
		
.. http:get:: /conceptschemes/{scheme_id}/c
    
    Search for concepts or collections in a scheme.
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes/TREES/c
        Host: localhost:6543
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Length:  117
        Content-Range:  items 0-2/3
        Content-Type:  application/json; charset=UTF-8
        Date:  Mon, 14 Apr 2014 14:47:33 GMT
        Server:  waitress

        [
            {
                "id": "1",
                "uri": "urn:x-skosprovider:TREES:1",
                "type": "concept",
                "label": "De Lariks"
            }, {   
                "id": "2",
                "uri": "urn:x-skosprovider:TREES:2",
                "type": "concept",
                "label": "De Paardekastanje"
            }, {   
                "id": 3,
                "uri": "urn:x-skosprovider:TREES:3",
                "type": "collection",
                "label": "Bomen per soort"
            }
        ]

    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes/PLANTS/c
        Host: localhost:6543
        Accept: application/json

    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 404 Not Found
        Content-Length:  775
        Content-Type:  text/html; charset=UTF-8
        Date:  Tue, 15 Apr 2014 20:32:52 GMT
        Server:  waitress

    :query type: Define if you want to show concepts or collections. Leave 
        blank to show both.
    :query mode: Allows for special processing mode for dijitFilteringSelect. 
        Makes it possible to use wildcards in the label parameter.
    :query label: Shows all concepts and collections that have this search
        string in one of their labels.
    :query collection: Get information about the content of a collection. 
        Expects to be passed an id of a collection in this scheme. Will restrict
        the search to concepts or collections that are a member of this collection
        or a narrower concept of a member.
    :query sort: Define if you want to sort the results by a given field. Otherwise items are returned
        in an indeterminate order. Prefix with '+' to sort ascending, '-' to sort descending.
        eg. ``?sort=-label`` to sort all results descending by label.

    :reqheader Range: Can be used to request a certain set of results.
        eg. ``items=0-24`` requests the first 25 results.
    :resheader Content-Range: Tells the client was set of results is being returned
        eg. ``items=0-24/306`` means the first 25 out of 306 results are being returned.
    :statuscode 200: The concepts in this conceptscheme were found.
    :statuscode 404: The conceptscheme was not found.
		
.. http:get:: /conceptschemes/{scheme_id}/c/{c_id}
    
    Get information about a concept or collection.
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes/TREES/c/1
        Host: localhost:6543
        Accept: application/json
    
    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Length:  316
        Content-Type:  application/json; charset=UTF-8
        Date:  Mon, 14 Apr 2014 14:49:27 GMT
        Server:  waitress

        {
            "broader": [],
            "narrower": [],
            "notes": [
                {"note": "A type of tree.", "type": "definition", "language": "en"}
            ], 
            "labels": [
                {"type": "prefLabel", "language": "en", "label": "The Larch"},
                {"type": "prefLabel", "language": "nl", "label": "De Lariks"}
            ], 
            "type": "concept", 
            "id": "1", 
            "uri": "urn:x-skosprovider:TREES:1",
            "related": [], 
            "label": "The Larch",
            "matches": {
                "close": [
                    'http://id.python.org/different/types/of/trees/nr/1/the/larch'
                ]
            },
            concept_scheme: {
                'uri': 'urn:x-foo:bar
            }
        }

    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes/TREES/c/4
        Host: localhost:6543
        Accept: application/json

    **Example response**:

    .. sourcecode:: http
        
        HTTP/1.1 404 Not Found
        Content-Length:  775
        Content-Type:  text/html; charset=UTF-8
        Date:  Tue, 15 Apr 2014 20:06:12 GMT
        Server:  waitress

    :statuscode 200: The concept was found in the conceptscheme.
    :statuscode 404: The concept was not found in the conceptscheme or the 
        conceptscheme was not found.


.. http:get:: /conceptschemes/{scheme_id}/c/{c_id}/displaychildren
    
    Get a list of Collections and Concepts that should be displayed as
    children of this Concept or Collection.
    
    **Example request**:
    
    .. sourcecode:: http
    
        GET /conceptschemes/TREES/c/3/displaychildren
        Host: localhost:6543
        Accept: application/json
    
    **Example response**:

    .. sourcecode:: http

        HTTP/1.1 200 OK
        Content-Type:  application/json; charset=UTF-8
        Date:  Mon, 14 Apr 2014 14:49:27 GMT
        Server:  waitress

        [
            {
                "id": "1",
                "uri": "urn:x-skosprovider:TREES:1",
                "type": "concept",
                "label": "De Lariks"
            }, {   
                "id": "2",
                "uri": "urn:x-skosprovider:TREES:2",
                "type": "concept",
                "label": "De Paardekastanje"
            }
        ]

    :statuscode 200: The concept was found in the conceptscheme.
    :statuscode 404: The concept was not found in the conceptscheme or the 
        conceptscheme was not found.
