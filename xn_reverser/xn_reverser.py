#!/usr/bin/env python3
import itertools
import json
import os
import string

import idna

# load unicode homoglyphs mappings json on import
mapping_file = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            "data/unicode_ascii_mappings.json"))
with open(mapping_file, "r") as f:
    mappings = json.load(f)


def xn_reverser(xn_domain):
    """Given a raw internationalized domain in xn-- form,
     enum possible ascii plaintext spoofs
    """

    domain_unicode = idna.decode(xn_domain)
    enum_data = {
        "domain_raw": xn_domain,
        "domain_idn_rendered": domain_unicode,
        "possible_spoofed_ascii": []
    }

    possible_chars = []

    possible_domain_words = []

    domain_parts = domain_unicode.split('.')
    for char in domain_parts[0]:
        # if char is regular ascii, add to list
        if char in string.printable:
            possible_chars.append([char])

        # mappings from homoglyphs lib can include ascii -> ascii spoofs such as 1-> l
        # https://stackoverflow.com/questions/3154301/what-should-itertools-product-yield-when-supplied-an-empty-list
        # (list must not be empty for itertools product)
        possible_chars.append(mappings.get(char, [""]))

    #print(possible_chars)
    possible_domain_words = list(itertools.product(*possible_chars))
    #print(possible_domain_words)

    possible_domains = [("{}.{}".format("".join(item), domain_parts[1]))
                        for item in possible_domain_words]
    enum_data["possible_spoofed_ascii"] = possible_domains

    return enum_data
