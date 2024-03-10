#!/usr/bin/env python3

import os
import sys
import glob

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please supply the path to a directory!")
        exit(1)

    dir_path = sys.argv[1]
    if not os.path.exists(dir_path):
        print(f"Directory could not be found: [{dir_path}]")
        exit(1)

    print('<table style="width: 100%; border: none;" cellspacing="0" cellpadding="0" border="0">\n<tr>\n', end='')
    dir_name = os.path.basename(dir_path)
    for webm_file in glob.glob(os.path.join(dir_path, '*.webm')):
        webm_file = os.path.basename(webm_file)
        print('<tr>\n  <td>\n      <video width="480p" controls>\n', end='')
        print(f'      <source src="https://github.com/4z3q/4z3q.github.io/blob/main/videos/{dir_name}/{webm_file}?raw=true" '
              f'type="video/webm">\n      </video>\n', end='')
        print(f'      <br/>\n      <br/>\n    </td>\n    <td valign="top">\nCOMMENT: {webm_file}\n    </td>\n  </tr>', end='')
    print('</table>')
