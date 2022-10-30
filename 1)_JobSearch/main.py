# Extracts the company name , skills required and posting date of python jobs from www.timesjobs.com
# User enters skills that he doesn't know... the program filters skills and displays jobs need the skills of the user
# Program automatically refreshes every hour

from bs4 import BeautifulSoup
import requests
import time

#Filter
unfamiliar_skill = input("Enter a skill you don't know seperated by space : ")
unfamiliar_skill_list = unfamiliar_skill.split()
unfamiliar_skill_list = [usl.lower() for usl in unfamiliar_skill_list] # Converting to lowercase
print("=== Filtering out skills ===")

# Function to search for jobs
def findJobs():

    # Linking the url and getting HTML data
    req = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
    html = req.text
    soup = BeautifulSoup(html,"html.parser")

    # List
    jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx") # This gives a list of all job details

    # enumerate is used to give automatic index as 1,2,3,4
    for index, job in enumerate(jobs):

        posted = job.find("span",class_="sim-posted").span.text.strip()

        # Searching based on "few days ago" in posted
        if "few" in posted:
            company_name = job.find("h3",class_="joblist-comp-name").text.strip()
            skills_required = job.find("span",class_="srp-skills").text.strip()

            # Converting to list and then lowercase
            skills_required_list = skills_required.split(",")
            skills_required_list = [sr.lower().strip() for sr in skills_required_list] 

            more_info = job.header.h2.a['href']
            
            # Filtering based on the skills u don't have
            flag = True
            for us in unfamiliar_skill_list:
                if us in skills_required_list:
                    flag = False
                    break
            
            # Printing individual jobs in individual files
            if flag==True:
                with open(f'1)_JobSearch//posts//{index}.txt','w') as file1:
                    file1.write("Company name : "+company_name+"\n")
                    file1.write("Skills required : "+skills_required+"\n")
                    file1.write("Posted : "+posted+"\n")
                    file1.write("More info : "+more_info+"\n")
                print(f'{index} File saved')


if __name__ == '__main__':
    while True:
        findJobs()
        time_wait = 10
        print("Waiting 60 minutes...")
        time.sleep(time_wait*60)


    