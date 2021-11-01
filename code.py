#to auto find
def job_finder():
    from bs4 import BeautifulSoup
    import requests
    import lxml
    import pandas as pd
    skills=input('Enter your skill for job application > ')
    unfamilar_skills=input('Enter the skill you are unfamilar with > ')
    loca=input('Enter your state location > ')
    e=input('Your work experience -{Years in integers} > ')
    file=input('Enter the file name you want to store > ')
    print('----------------------------------------------------------------------------------\n')
    data=pd.DataFrame(columns=['Company_Name','Skills_Required','Location','Experience_Required','Link for applying'])
    for j in range(0,5):
        page=requests.get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords={skills}&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&txtLocation={loca}&luceneResultSize=25&postWeek=60&txtKeywords={skills}&cboWorkExp1={e}&pDate=I&sequence=6&startPage={j}').text     
        soup=BeautifulSoup(page,'lxml')
        jobss=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
        for jobs in jobss:
            company_name=jobs.header.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skill=jobs.find('span',class_="srp-skills").text.replace(' ','')
            loc=jobs.find('ul',class_="top-jd-dtl clearfix")
            location=loc.span.text.replace(' ','')
            exp=loc.li
            experience=exp.text[11:]
            link=jobs.header.h2.a['href']
            posted=jobs.find('span',class_='sim-posted').span.text
            if 'few' in posted and unfamilar_skills not in skill:
                #print(f'Company name --> {company_name.strip()}\nSkills Required --> {skill.strip()}\nLocation --> {location}\nExperience Required --> {experience}\nLink for applying --> {link}')
                #print('--------------------------------------------------------------------------------------\n')
                data=data.append({'Company_Name':company_name.strip(),'Skills_Required':skill.strip(),'Location':location,'Experience_Required':experience,'Link for applying':link},ignore_index=True)
    data.to_excel(f'{file}.xlsx')
