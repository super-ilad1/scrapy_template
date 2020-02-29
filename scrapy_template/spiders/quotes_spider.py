# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['www.oxfordlearnersdictionaries.com']
    start_urls = []
    generate_url = lambda words: f'https://www.oxfordlearnersdictionaries.com/definition/english/{words}'

    with open("words_scrapy.jl", 'r', encoding='utf-8', errors='ignore') as read_file:
        for i in read_file.readlines():
            start_urls.append(generate_url((eval(i)['word'])))

    # 这里纪录笔记

    def parse(self, response):
        query = re.findall("https://www.oxfordlearnersdictionaries.com/definition/english/(\w*)", response.url)[0]

        soup = BeautifulSoup(response.text, 'lxml')

        concept = soup.select("span.def")[0].get_text()
        examples_list = [i.get_text() for i in soup.select("ul.examples > li")]

        if len(examples_list) > 5:
            examples_list = examples_list[0:5]

        count = 0
        for i in list(range(len(examples_list))):
            count += 1
            examples_list[i] = str(count) + ":" + examples_list[i]

        examples = "\n".join(examples_list)

        intros = concept + "\n" + "_" * 10 + "\n" + examples

        yield {
            "words": query,

            'intros': intros

        }
