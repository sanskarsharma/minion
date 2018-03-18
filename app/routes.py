from app import app_instance, db_instance, Config
from flask import render_template, flash, redirect, url_for, request
from flask import request

from datetime import datetime
import time
import random
from faker import Faker

import json

from werkzeug.urls import url_parse

from app.models import Links
import hashlib
from numpy import base_repr
import validators
from urllib.parse import urlparse



@app_instance.route("/fetch/short-url", methods=["POST", "GET"])
def fetch_short_url():

    long_url = ""

    if request.method == "POST" :
        long_url = request.form.get("long_url")
    elif request.method == "GET" :
        long_url = request.args.get("long_url")

    response_dict = {}


    if long_url == "" or long_url is None:
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["BAD_DATA"]

        response_json = json.dumps(response_dict)
        return response_json
    

    valid = validators.url(long_url)
    if not valid :
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["INVALID_URLS"]

        response_json = json.dumps(response_dict)
        return response_json

    short_url = get_short_url(long_url)

    response_dict["short_url"] = short_url
    response_dict["status"] = "OK"
    response_dict["status_codes"] = []
    
    response_json = json.dumps(response_dict)
    return response_json
 



@app_instance.route("/fetch/long-url", methods=["POST"])
def fetch_long_url():

    short_url = ""

    if request.method == "POST" :
        short_url = request.form.get("short_url")
    elif request.method == "GET" :
        short_url = request.args.get("short_url")

    response_dict = {}

    if short_url == "" or short_url is None:
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["BAD_DATA"]

        response_json = json.dumps(response_dict)
        return response_json


    parse_result = urlparse(short_url)


    print(parse_result.scheme)
    print(parse_result.netloc)
    print(parse_result.path)

    if parse_result.scheme != "" :

        if parse_result.netloc == Config.DOMAIN_NAME :
            path = parse_result.path[1:] 
            
            links_obj = Links.query.filter_by(short_url=path).first()
            
            if links_obj is None :
                response_dict["status"] = "FAILED"
                response_dict["status_codes"] = ["SHORT_URLS_NOT_FOUND"]
            
            else :
                long_url = links_obj.long_url

                response_dict["long_url"] = long_url
                response_dict["status"] = "OK"
                response_dict["status_codes"] = []

            response_json = json.dumps(response_dict)

            return response_json
    
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["SHORT_URLS_NOT_FOUND"]
        
        response_json = json.dumps(response_dict)

        return response_json
    
    else :

        domain = short_url.split("/")[0]
        path = short_url.split("/")[1]

        print(" domanin  " + domain)
        print(" path  " + path)

        if(domain != Config.DOMAIN_NAME) :

            response_dict["status"] = "FAILED"
            response_dict["status_codes"] = ["SHORT_URLS_NOT_FOUND"]
        
            response_json = json.dumps(response_dict)

            return response_json
    


        links_obj = Links.query.filter_by(short_url=path).first()
            
        if links_obj is None :
            response_dict["status"] = "FAILED"
            response_dict["status_codes"] = ["SHORT_URLS_NOT_FOUND"]
        
        else :
            long_url = links_obj.long_url

            response_dict["long_url"] = long_url
            response_dict["status"] = "OK"
            response_dict["status_codes"] = []

        response_json = json.dumps(response_dict)

        return response_json




@app_instance.route("/<short_url>", methods=["GET"])
def redirect_short_url(short_url):

    links_obj = Links.query.filter_by(short_url= short_url).first_or_404()

    if links_obj is not None :
        links_obj.count = links_obj.count + 1 
        db_instance.session.add(links_obj)
        db_instance.session.commit()


    return redirect(links_obj.long_url)


@app_instance.route("/fetch/count", methods=["POST"])
def count_usage():

    short_url = ""

    if request.method == "POST" :
        short_url = request.form.get("short_url")
    elif request.method == "GET" :
        short_url = request.args.get("short_url")

    response_dict = {}

    if short_url == "" or short_url is None:
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["BAD_DATA"]

        response_json = json.dumps(response_dict)
        return response_json


    domain = short_url.split("/")[0]
    path = short_url.split("/")[1]

    print(" domanin  " + domain)
    print(" path  " + path)


    if(domain != Config.DOMAIN_NAME) :

        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["SHORT_URLS_NOT_FOUND"]
    
        response_json = json.dumps(response_dict)

        return response_json


    links_obj = Links.query.filter_by(short_url=path).first()
        
    if links_obj is None :
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["SHORT_URLS_NOT_FOUND"]
    
    else :
        count = links_obj.count

        response_dict["count"] = count
        response_dict["status"] = "OK"
        response_dict["status_codes"] = []

    response_json = json.dumps(response_dict)

    return response_json



@app_instance.route("/fetch/short-urls", methods=["POST"])
def fetch_short_urls():
    
    long_urls = ""

    if request.method == "POST" :
        long_urls = request.form.get("long_urls")
    elif request.method == "GET" :
        long_urls = request.args.get("long_urlss")

    response_dict = {}


    if long_urls == "" or long_urls is None:
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["BAD_DATA"]

        response_json = json.dumps(response_dict)
        return response_json


    long_url_list = json.loads(long_urls)

    invalid_urls = []
    invalid_flag = False

    response_dict = {}

    for url in long_url_list :
        valid = validators.url(url)
        if not valid :
            invalid_flag = True
            invalid_urls.append(url)

    if(invalid_flag):
        response_dict["invalid_urls"] = invalid_urls
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["INVALID_URLS"]
        
        response_json = json.dumps(response_dict)
        return response_json

    short_urls_dict = {}
    for url in long_url_list :
        short_urls_dict[url] = get_short_url(url)
    
    response_dict["short_urls"] = short_urls_dict
    response_dict["invalid_urls"] = []
    response_dict["status"] = "OK"
    response_dict["status_codes"] = []
        
    response_json = json.dumps(response_dict)
    return response_json





@app_instance.route("/fetch/long-urls", methods=["POST"])
def fetch_long_urls():
    

    short_urls = ""

    if request.method == "POST" :
        short_urls = request.form.get("short_urls")
    elif request.method == "GET" :
        short_urls = request.args.get("short_urls")

    response_dict = {}

    if short_urls == "" or short_urls is None:
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["BAD_DATA"]

        response_json = json.dumps(response_dict)
        return response_json


    short_url_list = json.loads(short_urls)

    invalid_urls = []
    invalid_flag = False

    response_dict = {}

    for url in short_url_list :

        url_hash = url.split("/")[1]

        links_obj = Links.query.filter_by(short_url=url_hash).first()
        
        if links_obj is None :
            invalid_flag = True
            invalid_urls.append(url)

    if(invalid_flag):
        response_dict["invalid_urls"] = invalid_urls
        response_dict["status"] = "FAILED"
        response_dict["status_codes"] = ["SHORT_URLS_NOT_FOUND"]
        
        response_json = json.dumps(response_dict)
        return response_json

    long_urls_dict = {}
    
    for url in short_url_list :
        url_hash = url.split("/")[1]
        links_obj = Links.query.filter_by(short_url=url_hash).first()
        long_urls_dict[url] = links_obj.long_url

    
    response_dict["long_urls"] = long_urls_dict
    response_dict["invalid_urls"] = []
    response_dict["status"] = "OK"
    response_dict["status_codes"] = []
        
    response_json = json.dumps(response_dict)
    return response_json



    
@app_instance.route("/clean-urls", methods=["GET"])
def clean_urls():
    rows_deleted = Links.query.delete()
    db_instance.session.commit()
    return str(rows_deleted) + " rows deleted"
   









def get_short_url(long_url):

    timestamp = time.time()
    n = long_url + "__timestamp__"+str(timestamp)
    
    # getting md5 hash of long url
    hex_data = hashlib.md5(n.encode('utf-8')).hexdigest()
    scale = 16 # since md5 is hexdecimal
    num_of_bits = 128

	# converting md5 to binary t get oroginal 128 bit representation
    bin_str = str(bin(int(hex_data,scale))[2:].zfill(num_of_bits))

	# taking 32 bits
    bin_str_sliced = bin_str[:32]

    # for some calculated randomness
    if int(timestamp) % 2 == 0 :
        bin_str_sliced = get_another_slice(bin_str)


	# to get decimal value of the binary 43 bits
    deci = int(bin_str_sliced,2)
    
    short_url = str(base_repr(number=deci, base=36)).swapcase()

    links_obj = Links(long_url=long_url, short_url=short_url, count=0 )

    db_instance.session.add(links_obj)
    db_instance.session.commit()

    print(hex_data)
    print(bin_str)
    print(bin_str_sliced)
    print(deci)
    print(short_url)


    # adding domain name before returning
    short_url = Config.DOMAIN_NAME + "/" + short_url    

    return short_url



def get_another_slice(bin_str):
    rng = 3
    if "1" in bin_str[32:32+rng] :
        return bin_str[32:64]
    elif "1" in bin_str[64:64+rng] :
        return bin_str[64:96]
    else:
        return bin_str




























    

    