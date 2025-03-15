import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

sql_file=r"D:\MAAB academy new\python\homework\lesson-12\homework\jobs.db"
csv_sourse=f"D:\MAAB academy new\python\homework\lesson-12\homework\filtered_jobs.csv"


def scrape_jobs():
    url="https://realpython.github.io/fake-jobs"
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")

    job_listings=[]
    jobs=soup.find_all('div', class_='card-content')

    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        description = job.find("div", class_="content").text.strip()
        application_link = job.find("a", string="Apply").get("href")

        job_listings.append((title, company, location, description, application_link))

    return job_listings

def init_db():
    with sqlite3.connect(sql_file) as con:
        cursor=con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_title TEXT,
                company TEXT,
                location TEXT,
                description TEXT,
                application_link TEXT,
                UNIQUE(job_title, company, location)
        )
""")
        
def store_jobs(job_listings):
    conn = sqlite3.connect(sql_file)
    cursor = conn.cursor()

    for job in job_listings:
        title, company, location, description, application_link = job

        # Check if the job already exists
        cursor.execute("""
            SELECT description, application_link FROM jobs
            WHERE job_title = ? AND company = ? AND location = ?
        """, (title, company, location))

        existing_job = cursor.fetchone()

        if existing_job:
            # If job exists, check if details have changed
            if existing_job[0] != description or existing_job[1] != application_link:
                cursor.execute("""
                    UPDATE jobs
                    SET description = ?, application_link = ?
                    WHERE job_title = ? AND company = ? AND location = ?
                """, (description, application_link, title, company, location))
        else:
            # If job is new, insert it
            cursor.execute("""
                INSERT INTO jobs (job_title, company, location, description, application_link)
                VALUES (?, ?, ?, ?, ?)
            """, job)

    conn.commit()
    conn.close()

# Step 4: Filter job listings by location or company
def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(sql_file)
    cursor = conn.cursor()
    
    query = "SELECT * FROM jobs WHERE 1=1"  # Always true to simplify filtering logic
    params = []
    
    if location:
        query += " AND location = ?"
        params.append(location)
    if company:
        query += " AND company = ?"
        params.append(company)

    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()

    return results


# Step 5: Export filtered jobs to CSV (Without Pandas)
def export_to_csv(location=None, company=None, filename=csv_sourse):
    jobs = filter_jobs(location, company)

    if jobs:
        columns = ["ID", "Job Title", "Company", "Location", "Description", "Application Link"]
        
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(columns)  # Write header
            writer.writerows(jobs)  # Write job data

        print(f"Filtered jobs exported to {filename}")
    else:
        print("No matching jobs found.")

# Main Execution
if __name__ == "__main__":
    print("Initializing database...")
    init_db()

    print("Scraping job listings...")
    jobs = scrape_jobs()

    print("Storing jobs in the database...")
    store_jobs(jobs)

    print("Scraping and storing completed successfully!")
