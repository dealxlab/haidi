# haidi

![haidi logo](https://github.com/vladimirghetau/haidi/blob/master/logo_small.png?raw=true)

_Haidi is "The" Artificially Intelligent Big Data Integration Tools Suite for Data Lakes_

## What is it?

Got the data lake in place, all the data is in, but nothing makes sense. 

**Haidi** is providing automatic ETL, BI and Reporting by relying on machine learning and artificial intelligence techniques in order to produce the following desired outcomes:

 * *Intelligent datasets analysis*: 
  * relies on metadata extracted from all the datasets in your data lake
  * proof-of-work: being able to automatically integrate RBDMS schemas
  * NoSQL datasets
  * Natural Language datasets
 * *Intelligent datasets pre-integration*: benchmarks and classifies the possibilities and how hard/easy it is to integrate the identified datasets.
 * *Autointegration*: the ability to integrate nonhomogenous datasets automatically, and be able to offer a prediction score for each business operation (in advance, real time)
 * *Automatic business intelligence extraction*: we would ideally like to maintain a database of libraries / modules which we keep building, designed specifically for each industry
 * *Automatic reporting*: a generic, basic, extendable reporting system which does not need human input, but maybe generic rules (out of the box), or custom business rules (customisable by each data lake owner)
 

## Participate!

We are currently looking for programmers who are interested in participating in this project. 

Decisions made until now (Subject to change if required): 
 * __14th Feb 2017__
  * Project Domain Area Scope
  * Programming Language: Python
 * __20th Feb 2017__
  * Basic 1st iteration of working version of a cataloguing system (File System and S3): this will be used to collect all the meta data from various sources in order to further analyse the functional and non-functional requirements. We would like to ask as many members to volunteer and collect meta-data that can be shared with our team in order to grow the product.
 
Decisions to be made: 
 * License choice (Apache, MIT, etc, etc) - looking for contributors
 * Architecture: RUP (UML based)
 * Libraries: identify a business rules library for Python

## Researchers, Documentation

We shall maintain a list of links that helped develop the product

## Installation

*Please note*: We are still exploring the requirements, and for now we would need as much meta-data as possible from your data lake. Please use the instructions below on how you can index your meta data before you send it to us to further expand the project.

The instructions below are for Ubuntu 14.04 64bit, but can be used in any Python 2.7+ environment: 

 * Install Python + PIP
 * pip install docopt pyyaml boto
 * Clone the Haidi repository
 * cd haidi/bin
 * Launch the Indexer / Cataloguing Meta data scanner and point it to your data folder / AWS S3 storage bucket
 * zip the file and send it to us, or simply upload it into the `sample_data/catalogue_metadata/` folder

### AWS S3 IAM Policy

Please note, alternativelly, instead of setting the AWS login information inside the cfg/haidi.yml file, you can set up the following two env vars: `AWS_ACCESS_KEY_ID` (Your AWS Access Key ID) and `AWS_SECRET_ACCESS_KEY` (Your AWS Secret Access Key). (todo: onliner to populate ~/.bashrc and load it again). Env vars supersede haidi.yml variables.

Create a user called `haidi-indexer` into your AWS IAM console interface, enable programmatic access (Access Type section) so you can write down the `ACCESS_KEY_ID` and `SECRET_ACCESS_KEY` values, you'll have to put them in `cfg/haidi.yml`.
Create a group called `haidi-indexer` as well, and attach the `AmazonS3ReadOnlyAccess` policy type to this group. Next, add the `haidi-indexer` user to the `haidi-indexer`.

TODO: CloudFormation automation of Haidi indexer setup so anyone can easily create and configure the permissions.

Sample usage: 

```python catalogue.py index s3://haididw/```

## Get Involved

Please lookup for "todo" inside the project. If you want to dive into code, just read the .md file having the same name as the CLI tool itself, and you'll see the plan in there on what needs to be done.

If you would like more information on how to participate to this project, please contact the [project lead](https://github.com/vladimirghetau/)

## Acknowledgements

Hands graphic by [Freepik](http://www.flaticon.com/authors/freepik), licensed under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/), made with [Logo Maker](http://logomakr.com).
Haidi ASCII Logo on displayed when launching CLI tools, by [patorjk](http://patorjk.com/software/taag/#p=display&h=0&v=0&f=Isometric1&t=Haidi)