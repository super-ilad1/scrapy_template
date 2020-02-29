# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re

class WordsScrapySpider(scrapy.Spider):
    name = 'words_scrapy'
    allowed_domains = ['www.examword.com']
    start_urls = ['https://www.examword.com/ielts-list/4000-academic-word-1?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-2?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-3?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-4?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-5?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-6?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-7?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-8?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-9?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-10?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-11?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-12?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-13?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-14?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-15?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-16?la=en/',
'https://www.examword.com/ielts-list/4000-academic-word-17?la=en/']


    def parse(self, response):
        # page_generate = lambda page: f'https://www.examword.com/ielts-list/4000-academic-word-{page}?la=en/'

        soup = BeautifulSoup(response.text, 'lxml')
        words = [i.get_text() for i in  soup.select("#centerCoreVocabulary > div[id^='i_ielts']")]

        for i in words:
            yield{
                "word":i
            }








