from fastapi import FastAPI, Query
from typing import Annotated, List
import random

app=FastAPI()

#initialize dummy database for 100 skills workers
first_names = ["Alice","Bob","Charlie","Diana","Ethan","Fiona","Hannah","Isaac","Jane"]
last_names = ["Johnson","Smith","Lee","Prince","Hunt","Glenanne","Bluth","Baker","Newton","Doe"]

skills_list = ["Python", "SQL", "JavaScript", "React", "Django", "Flask", "Pandas", "NumPy", "Node.js", "HTML", "CSS", "Java", "C++"]

people_data = []
for i in range(1, 101):
    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    person = {
        "id": i,
        "name": full_name,
        "skills": ", ".join(random.sample(skills_list, random.randint(2, 5))),
        "location": random.choice(["NYC", "LA", "Chicago", "Houston", "Seattle", "Austin", "Boston", "San Francisco", "Atlanta"]),
        "job_title": random.choice(["Data Analyst", "Software Engineer", "Data Scientist", "Frontend Developer", "Backend Developer", "Full Stack Developer", "DevOps Engineer"]),
        "profile_summary": f"This is a placeholder profile summary for {full_name}."
    }
    people_data.append(person)