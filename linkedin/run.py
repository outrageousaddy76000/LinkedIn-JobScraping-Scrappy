# run_spider.py
from urllib.parse import quote
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from linkedin.spiders.linkedin_fetch_jobs import LinkedinJobsSpider

# Define job titles
job_titles_input = input("Enter job titles separated by comma: ")

# Encode job titles properly
job_titles_list = [quote(title.strip()) for title in job_titles_input.split(',')]

# Create a CrawlerProcess
process = CrawlerProcess(get_project_settings())

# Run the spider with job_titles as argument
process.crawl(LinkedinJobsSpider, job_titles=job_titles_list)
process.start()
