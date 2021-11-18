# import pandas
import pandas as pd

# ** Read Salaries.csv as a dataframe called sal.**
sal = pd.read_csv("2_pandas_Salaries.csv")

# ** Check the head of the DataFrame. **
sal_head = sal.head()
# print(sal_head)

# ** Use the .info() method to find out how many entries there are.**
sal_info = sal.info()
# print(sal_info)

# **What is the average BasePay ?**
avg_base_pay = sal['BasePay'].mean()
# print(avg_base_pay)

# ** What is the highest amount of OvertimePay in the dataset ? **
max_over_time = sal['OvertimePay'].max()
# print(max_over_time)

# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you
# may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **
job_title_jd = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
# print(job_title_jd)

# ** How much does JOSEPH DRISCOLL make(including benefits)? **
total_pay_jd = sal[sal['EmployeeName'] ==
                   'JOSEPH DRISCOLL']['TotalPayBenefits']
# print(total_pay_jd)

# ** What is the name of highest paid person (including benefits)?**
high_pay_person = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
# print(high_pay_person)

# ** What is the name of lowest paid person (including benefits)? Do you notice something
#  strange about how much he or she is paid?**
low_pay_person = sal[sal['TotalPayBenefits'] ==
                     sal['TotalPayBenefits'].min()]
# print(low_pay_person)

# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
avg_base_2011_2014 = sal.groupby('Year').mean()['BasePay']
# print(avg_base_2011_2014)

# ** How many unique job titles are there? **
unique_job = sal['JobTitle'].nunique()
# print(unique_job)

# ** What are the top 5 most common jobs? **
top5_jobs = sal['JobTitle'].value_counts().head(5)
# print(top5_jobs)

# ** How many Job Titles were represented by only one person in 2013?
#  (e.g. Job Titles with only one occurence in 2013?) **
jb_occurrence = sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)
print(jb_occurrence)
