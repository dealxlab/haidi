## Catalogue Tool

The catalogue.py CLI tool will:

- go to S3 / local file system
- index metadata: extract the table heads, structural info of all the files supported by Haidi
- store the timestamp of each indexing job and parsed file
- prep the metadata in a format that will be suitable for the AI component
- to participate, just lookup "todo" in the py file
- CI / CD will come up once the project grows in the number of participants and source code footprint

## Example 

`$ python catalogue.py --help`

```
  _    _           _       _   _ 
 | |  | |         (_)     | | (_)
 | |__| |   __ _   _    __| |  _ 
 |  __  |  / _` | | |  / _` | | |
 | |  | | | (_| | | | | (_| | | |
 |_|  |_|  \__,_| |_|  \__,_| |_|
                                 
                                 
Haidi v0.0.1- "The" Artificially Intelligent Big Data Integration Tools Suite for Data Lakes

Haidi Catalogue CLI Tool

Usage:
  catalogue.py [-h | --help] [-v | --version]
  catalogue.py index PATH

Options:
  -h --help     Show this screen.
  -v --version  Show version.
 
Commands:
  index PATH  Index the specified PATH, it can be file system or AWS S3 path to bucket or folder.
```