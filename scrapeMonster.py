import webbrowser
import urllib2
import re
import csv
import sys
sys.path.append('/Users/Almightyeric/Desktop/python/BeautifulSoup')
from bs4 import BeautifulSoup

csvout = open("MonsterData.csv", "wb")
writecsv=csv.writer(csvout)

# ins = open( "AmazonUrls.txt", "r" )
ins=[]

edu=""
cat=""


for n in range (1,2):
	if n==0:
		edu="High-School"

	else:
		edu="Associate-Degree"

	for m in range (7,14):
		if m==0:
			cat="Biotech-R-D-Science"

		elif m==1:
			cat="Building-Construction-Skilled-Trades"

		elif m==2:
			cat="Customer-Support-Client-Care"

		elif m==3:
			cat="Engineering"

		elif m==4:
			cat="Food-Services-Hospitality"

		elif m==5:
			cat="Human-Resources"

		elif m==6:
			cat="Installation-Maintenance-Repair-search"

		elif m==7:
			cat="Logistics-Transportation"

		elif m==8:
			cat="Manufacturing-Production-Operations"

		elif m==9:
			cat="Medical-Health"

		elif m==10:
			cat="Project-Program-Management"

		elif m==11:
			cat="Quality-Assurance-Safety"
		elif m==12:
			cat="Security-Protective-Services"
		else:
			cat="other"

		for page in range(1,50):
			ins.append("http://jobsearch.monster.com/search/%s_4?eid=%sl&pg=%s&salmin=30000&saltyp=1&nosal=false"%(cat,edu,page))

			# print "http://jobsearch.monster.com/search/%s_4?eid=%sl&pg=%s&salmin=30000&saltyp=1&nosal=false"%(cat,edu,page)
# ins.append("http://jobsearch.monster.com/search/Installation-Maintenance-Repair_4?eid=High-School&pg=14&salmin=30000&saltyp=1&nosal=false")
# ins.append("http://jobsearch.monster.com/search/?eid=Associate-Degree&pg=8&salmin=30000&saltyp=1&nosal=false")  
data=["Title","Company","Location","Salary","Min_Salary","Max_Salary","Page","Category","State","Education"]
writecsv.writerow(data)
data=[]
dataTitle=[]
dataPage=[]
dataCompany=[]
dataAddress=[]
dataSalary=[]
dataCategory=[]
dataState=[]
dataSalaryMin=[]
dataSalaryMax=[]
dataEdu=[]


for line in ins:

	line=line.strip()

	if "Building" in line:
		dataCategory.append('Building Construction/Skilled Trades')
	elif "Biotech" in line:
		dataCategory.append('Biotech /R&D /Science')

	elif "Customer" in line:
		dataCategory.append('Customer Support /Client Care')
	elif "Engineering" in line:
		dataCategory.append('Engineering')
	elif "Food" in line:
		dataCategory.append('Food Services/Hospitality')
	elif "Resources" in line:
		dataCategory.append('Human Resources')
	elif "Maintenance" in line:
		dataCategory.append('Installation, Maintenance Repair search')
	elif "Transportation" in line:
		dataCategory.append('Logistics/Transportation')
	elif "Manufacturing" in line:
		dataCategory.append('Manufacturing, Production Operations')
	elif "Medical" in line:
		dataCategory.append('Medical Health')
	elif "Management" in line:
		dataCategory.append('Project Program Management')
	elif "Assurance" in line:
		dataCategory.append('Quality/Assurance /Safety')
	elif "Security" in line:
		dataCategory.append('Security/Protective Services')

	else:
		dataCategory.append('Other')


	if "High-School" in line:
		dataEdu.append("High School")
	else:
		dataEdu.append('Associate Degree')



	# print(line)
	page = urllib2.urlopen(line)
	value = page.read()
	soup = BeautifulSoup(value)

	titles=soup.find_all("a",class_="slJobTitle fnt11")
	for i in titles:
		title=i.string
		href=i["href"]
		title=title.encode("utf8","replace")
		href=href.encode("utf8","replace")
		dataTitle.append(title)
		dataPage.append(href)

	
	addresses=soup.find_all("div", class_="jobLocationSingleLine")
	for i in addresses:
		if (i.a):
			address=i.a.string
			address=address.encode("utf8","replace")
			dataAddress.append(address)

			state_address=address.split(",")
			try:
				if state_address[1]:
					state=state_address[1]
					dataState.append(state)
				else:
					dataState.append("N/A")
			except Exception, e:
				dataState.append("N/A")

			


		else:
			dataAddress.append("N/A")



	companies=soup.find_all("div", class_="companyContainer")
	for i in companies:
		company=i.a.next_sibling["title"]
		company=company.encode("utf8","replace")
		dataCompany.append(company)


	salaries=soup.find_all("div",class_="fnt13")
	for i in salaries:
		salary=i.string.strip()

		salary=salary.encode("utf8","replace")
		

		dataSalary.append(salary)
		salary_range=salary.split("-")

	
		
		if len(salary_range)==1:
			salary_min=salary_range[0]
			salary_max=salary_range[0]
			salary_min=salary_min.encode("utf8","replace")
			salary_max=salary_max.encode("utf8","replace")
		else:
			# if len(salary_range[0])>7:
			salary_min=salary_range[0]
			salary_max=salary_range[1]
			salary_min=salary_min.encode("utf8","replace")
			salary_max=salary_max.encode("utf8","replace")


		

			# else:
			# 	a="".join(salary_range[0].split("$")).split(".")[0]
	
			# 	b="".join(salary_range[1].split("$")).split(".")[0]

			# 	a=int(a)
			# 	b=int(b)

			# 	salary_num=(a/10)*20800
			# 	salary_num1=(b/10)*20800
			# 	salary_min="$"+str(salary_num)
			# 	salary_max="$"+str(salary_num1)


		dataSalaryMin.append(salary_min)
		dataSalaryMax.append(salary_max)



 

	for i in range(0,len(dataAddress)):
		data.append(dataTitle[i])
		data.append(dataCompany[i])
		data.append(dataAddress[i])
		data.append(dataSalary[i])
		data.append(dataSalaryMin[i])
		data.append(dataSalaryMax[i])
		data.append(dataPage[i])
		data.append(dataCategory[0])
		data.append(dataState[i])
		data.append(dataEdu[0])

		writecsv.writerow(data)
		data=[]
	
	data=[]
	dataAddress=[]
	dataCompany=[]
	dataPage=[]
	dataTitle=[]
	dataCategory=[]
	dataState=[]
	dataSalaryMin=[]
	dataSalaryMax=[]
	dataEdu=[]
	dataSalary=[]




	
		