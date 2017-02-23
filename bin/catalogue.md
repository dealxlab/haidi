The catalogue.py CLI tool will:

- go to S3 / local file system
- index metadata: extract the table heads, structural info of all the files supported by Haidi
- store the timestamp of each indexing job and parsed file
- prep the metadata in a format that will be suitable for the AI component
- to participate, just lookup "todo" in the py file
- CI / CD will come up once the project grows in the number of participants and source code footprint