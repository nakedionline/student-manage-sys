#!/usr/bin/python
import urllib
from bs4 import BeautifulSoup
import json
import sys
#********************************************
#*
#* Nakedi Mabusela
#* Scraper Proof of Concept - Unisa University
#*
#********************************************
class QualificationDetail:
      def __init__(self, institution,name, qualificationCode, nqfLevel,totalCredits, apsScoring):
          self.institution = institution;
          self.name = name;
          self.qualificationCode = qualificationCode;
          self.nqfLevel = nqfLevel;
          self.totalCredits = totalCredits;
          self.apsScoring = apsScoring;

      def jsonFy(self,data,high_level_tag):
         if not data:
            data = {};
            data[high_level_tag] = [];

         data[high_level_tag].append({
            'institution': self.institution,
            'name': self.name,
            'qualificationCode': self.qualificationCode,
            'nqfLevel': self.nqfLevel,
            'totalCredits': self.totalCredits,
            'apsScoring': self.apsScoring
         })

         return data;

def scrape_qualification_page(url):

    url = urllib.quote(url.encode('utf8'), ':/')

    print "About to open : "+url;

    edu_page = urllib.urlopen(url);
    soup = BeautifulSoup(edu_page, 'html.parser')
    qualification = soup.find('h3',text='Undergraduate qualifications');
    qualification_name =  qualification.find_next('h1').contents[0];
    qualification_code = qualification.find_next('td',text='Qualification code:').find_next().contents[0];
    qualification_NQF_level = qualification.find_next('td',text='NQF level:').find_next().contents[0];
    qualification_total_credits = qualification.find_next('td',text='Total credits:').find_next().contents[0];
    qualification_APS_scoring = qualification.find_next('td',text='APS/AS:').find_next().contents[0];

    return  QualificationDetail('unisa',qualification_name,qualification_code,qualification_NQF_level,qualification_total_credits,qualification_APS_scoring);

unisa_qualifications_page = 'https://www.unisa.ac.za/sites/corporate/default/Apply-for-admission/Undergraduate-qualifications/Qualifications/All-qualifications'

page = urllib.urlopen(unisa_qualifications_page)

soup = BeautifulSoup(page, 'html.parser')

h2_qualifications = soup.find('h2', text="Higher Certificates");

qualification_link_data = h2_qualifications.find_next('li');

qualifiction_parameters = {};
qualifiction_parameters = [['higherCertificate','Higher-Certificate','data-higher-certificate.json'],['diploma','Diploma-','data-diploma.json']];

qualification_index = int(sys.argv[1]);
jsonData = {};
jsonDataName = qualifiction_parameters[qualification_index][0];
jsonData[jsonDataName] = [];

while qualification_link_data :
    qualification_link_data = qualification_link_data.find_next('li');
    
    if qualification_link_data  :
        link = qualification_link_data.find('a');
        url = link.get('href') ;
        if  -1 == url.find(qualifiction_parameters[qualification_index][1]):
            continue;
        qualification_detail = scrape_qualification_page("https://www.unisa.ac.za"+url);
        jsonData = qualification_detail.jsonFy(jsonData,qualifiction_parameters[qualification_index][0]);

with open('./output/'+qualifiction_parameters[qualification_index][2], 'w') as outfile:  
    json.dump(jsonData, outfile)






