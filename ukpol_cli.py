#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import click
from click import echo, style
import re

POSTCODEURL = 'http://uk-postcodes.com/postcode/'
POLICEAPI = 'http://data.police.uk/api/'

__version__ = "0.0.1"
__author__ = "Doug Bromley"
__license__ = "MIT"


@click.group(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '--version', '-v', message='%(version)s')
def cli():
    """The UK Police CLI. Find out data and info based on a UK postcode.

    \b
    Examples:
        \b
        ukpol area B610PL
        ukpol force SK224PL
        ukpol contact PE227DB
        ukpol crimes B458ES
    \b
    Do not put a space inside the postcode!
    To get help with a subcommand, add the --help option after the command.
    """
    pass


@cli.command()
@click.argument('postcode')
def area(postcode):
    force, area = get_area_from_postcode(postcode)
    print("")
    areainfo = get_area_info(force, area)

    echo(
        style("%s is covered by %s" % (
            style(postcode, fg='green'), style(format_data_title("%s %s" % (force, 'Constabulary')), fg='blue')
        ))
    )

    output_header("Contact Info")
    print_contact_info(areainfo['contact_details'])

    output_header("Description")
    print_area_description(re.sub('<[^<]+?>', '', areainfo['description']))


@cli.command()
@click.argument('postcode')
def contact(postcode):
    force, area = get_area_from_postcode(postcode)
    areainfo = get_area_info(force, area)

    output_header("Contact Info for %s" % format_data_title(force))
    print_contact_info(areainfo['contact_details'])


@cli.command()
@click.argument('postcode')
@click.option('--list', default=False)
def force(postcode):
    force, area = get_area_from_postcode(postcode)
    echo(
        style("%s is covered by %s Constabulary" % (
            style(postcode, bold=True), style(format_data_title(force), fg='blue')
        ))
    )

    fi = get_force_info(force)
    format_info_line('Telephone', fi['telephone'])
    format_info_line('Website', fi['url'])
    #format_info_line('Description', fi['description']) rarely any have one
    print_engagement_methods(fi['engagement_methods'])


@cli.command()
@click.argument('postcode')
@click.option(
    '--date',
    help='Optional. (YYYYMM) Limit results to a specific month.'
)
def crimes(postcode, date=None):
    loc = get_coords_from_postcode(postcode)
    crimes = street_level_crimes(loc['lat'], loc['lng'], date)
    print_crimes_info(crimes)


def street_level_crimes(lat, lng, crimedate=None):
    req_url = ''.join([
        POLICEAPI,
        'crimes-street/all-crime?lat=',
        str(lat),
        '&lng=',
        str(lng)
    ])
    if crimedate:
        req_url = "%s&date=%s-%s" % (req_url, crimedate[0:4], crimedate[4:6])

    resp = requests.get(req_url).json()
    return resp


def area_level_crime(lat, lng, crimedate=None):
    pass


def format_info_line(title, info):
    try:
        echo(
            '%s: %s' % (style(title.ljust(10), fg='blue'), style(info.ljust(10)))
        )
    except AttributeError:
        print title


def get_area_info(force, area):
    requrl = ''.join([POLICEAPI, force, '/', area])
    return requests.get(requrl).json()


def get_force_info(force):
    requrl = ''.join([POLICEAPI, 'forces/', force])
    return requests.get(requrl).json()


# Print util functions


def format_data_title(name):
    """Fromats key values by removing hyphes and title() the string"""
    return name.replace('-', ' ').title()


def output_header(header):
    print("")
    echo(style(header, bold=True, fg='blue'))
    echo(('*') * len(header))


# Area establishment functions

def get_area_from_postcode(postcode):
    return get_area_from_coords(
        get_coords_from_postcode(postcode)
    )


def get_coords_from_postcode(postcode):
    """Using UK Postcodes API get the lat/lng coordinates of a given postcode"""
    try:
        requrl = '%s%s.json' % (POSTCODEURL, postcode)
        loc = requests.get(requrl).json()['geo']
    except KeyError:
        echo(
            style(
                "Location not found - please make sure postcodes are entered in full without a space",
                fg='red'
            )
        )
        sys.exit(0)
    return loc


def get_area_from_coords(loc):
    """Using the Police API make a call to 'locate-neighbourhood' to get the
    force and neghbourhood that cover that area"""
    req_url = ''.join([
        POLICEAPI,
        'locate-neighbourhood?q=',
        str(loc['lat']),
        ',',
        str(loc['lng'])
    ])
    resp = requests.get(req_url).json()

    return resp['force'], resp['neighbourhood']


# Print functions

def print_crimes_info(crimes):
    """Given a dicttionary of crimes print out the info as a list"""
    for crime in crimes:
        try:
            echo("%s%s%s" % (
                style(
                    format_data_title(crime['category'].ljust(25)),
                    fg='red'
                ),
                style(
                    format_data_title(crime['month'].ljust(10)),
                    fg='blue'
                ),
                style(
                    format_data_title(crime['location']['street']['name'].ljust(30))
                )
            ))
        except TypeError:
            print('Somethign went wrong')
            print(crime['category'])


def print_contact_info(details):
    """Given a dictionary of the detals print out the contact info in column list format"""
    tel = False
    for key, val in details.items():
        if key == 'telephone':
            tel = True
        echo('%s: %s' % (style(key.ljust(10), fg='blue'), style(val.ljust(20))))

    if not tel:
        echo('%s: %s' % (style('Telephone'.ljust(10), fg='blue'), style('101'.ljust(10))))


def print_area_description(desc):
    if desc:
        echo(desc)
        return

    echo(style("No Description", fg='red'))


def print_engagement_methods(methods):
    for method in methods:
        echo('%s: %s' % (style(method['title'].ljust(10), fg='blue'), style(method['url'].ljust(20))))
