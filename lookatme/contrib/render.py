#!/usr/bin/env python3

"""
An image renderer that uses ueberzug
"""


import os
import re
import subprocess
import tempfile
from typing import List, Dict
import urwid
import distutils.spawn


from lookatme.render.markdown_inline import image as lookatme_image
from lookatme.exceptions import IgnoredByContrib


RENDERERS = {
    "graphviz": {
        "langs": ["dot", "graphviz"],
        "exe": "dot",
        "args": [
            "-Gdpi=400", "-Tpng", "-o", "{{OUTPATH}}", "{{INPATH}}",
        ]
    },
    "mermaid": {
        "langs": ["mermaid"],
        "exe": "mmdc",
        "args": [
            "-i", "{{INPATH}}", "-o", "{{OUTPATH}}",
        ]
    }
}

def render_code(token: Dict, body: urwid.Widget, stack: List[urwid.Widget], loop: urwid.MainLoop):
    lang = token["lang"] or ""

    renderer = None
    image_height = "20"
    for rend_name, rend_info in RENDERERS.items():
        for rend_lang in rend_info["langs"]:
            match = re.match("{}-?(\d*)".format(rend_lang), lang)
            if match is not None:
                renderer = rend_info
                if match.group(1) != "":
                    image_height = match.group(1)
                break

    if renderer is None:
        raise IgnoredByContrib()
    if distutils.spawn.find_executable(renderer["exe"]) is None:
        raise IgnoredByContrib()

    infd, infile = tempfile.mkstemp()
    pngfd, pngfile = tempfile.mkstemp(".png")

    with open(infd, "w") as f:
        f.write(token["text"])

    args = [renderer["exe"]] + renderer["args"]
    for idx in range(len(args)):
        args[idx] = args[idx].replace("{{INPATH}}", infile)
        args[idx] = args[idx].replace("{{OUTPATH}}", pngfile)

    proc = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    stdout, stderr = proc.communicate()
    return urwid.Pile(lookatme_image(pngfile, image_height, image_height))
