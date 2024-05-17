# Nestor
## Before running
Before running the Django app for the first time you have to run: 
```
pip install -r requirements.txt 
```

### Accounts:
- All passwords: egerforseti
- Employee username:
  - Ísland: gudnith
- Applicant usernames
  - katrinjak, baldurth, steinunnolina, eirikuringi, baldurth, hallahrund 
hallatomas, asthormagnusson, helgathoris, asdisran, katrinjak, jongnarr, arnarthor



## Extra requirements

### Responsive design 

### Skills
- Skills were added to the application process
- In admin, we can add more skill genres and add more skills in each skill
genre which makes it easier to access the correct skills (filter the skills)

### Virtual CV
- The website lets a user create a Virtual CV. Here they can;
  - Edit their contact information
  - Add/Edit/Delete Experiences
  - Add/Edit/Delete Education
  - Add/Edit/Delete References
  - Add/Delete Skills
- These CV attributes are then copied over to the user's application when they initiate the application process. 
- During the application process, the user can further edit the Virtual CV to make it more specific to the job he is applying for, without changing any of the attributes in his original Virtual CV

### Extra Requirements in Job Search
- It is possible to filter jobs by location (country)
- It is possible to filter by job name and company name, in either direction
  - for ex. alphabetical and reverse alphabetical order

### Extra Requirements in Company search
- It is possible to sort by company name
- It is possible to filter by location and search for a company by name in the search bar

### Favorite jobs
- A user [ type: applicant ] can favorite a job from the job's page, and also un-favorite
- The "heart" icon on a job's job card is displayed as filled-in if the user has added it to favorite jobs 
- User can see a list of all his favorite jobs in the navigation bar option: "Favorite Jobs"

### Company profile 
- Website admins can create company profiles and add/change employee access to said company data
- Employees that are assigned to a campany account can also see/edit their own contact information

### Job offers
- Users [ type: employee ] have the following abilities:
  - Create Jobs offers for their company
  - Ask website admins to edit the "is_available" job attribute to indicate if the job position has been filled
  - See a list of the jobs they (or the company) have published
  - See a list of all applicants that have applied for a specific job offer
  - Get a detailed overview of an applicants application
    - contact info / cover letter / experience / education / references / skills