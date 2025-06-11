from fastapi import FastAPI, Query
from typing import Annotated, List
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#initialize dummy database for 100 skills workers
first_names = ["Alice","Bob","Charlie","Diana","Ethan","Fiona","Hannah","Isaac","Jane","John","kelvin","Morgan"]
last_names = ["Johnson","Smith","Lee","Prince","Hunt","Glenanne","Bluth","Baker","Newton","Doe","Harry","Torre"]

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
    
@app.get("/search")
async def search_people(name:Annotated[str, Query(..., min_length=1)]):
    results = [p for p in people_data if name.lower() in p["name"].lower()]
    return {"results": results}

@app.get("/skill_analysis")
async def analyze_skills(name:Annotated[str, None]=None):
    matches = [p for p in people_data if name.lower() in p["name"].lower()]
    skill_count = {}
    for p in matches:
        skills = p["skills"].split(", ")
        for s in skills:
            skill_count[s] = skill_count.get(s, 0) + 1
    return {"skills": skill_count}

@app.get("/trends")
async def get_trends():
    all_skills = []
    for p in people_data:
        all_skills.extend(p["skills"].split(", "))
    trend_count = {}
    for s in all_skills:
        trend_count[s] = trend_count.get(s, 0) + 1
    return {"top_skills": trend_count}