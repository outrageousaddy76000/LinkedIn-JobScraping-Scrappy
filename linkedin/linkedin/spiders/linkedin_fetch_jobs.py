import scrapy
from scrapy.http import Request
import re
import pandas as pd
from datetime import datetime

class LinkedinJobsSpider(scrapy.Spider):
    name = 'linkedin_fetch_jobs'
    allowed_domains = ['linkedin.com']

    def __init__(self, job_titles=None, *args, **kwargs):
        super(LinkedinJobsSpider, self).__init__(*args, **kwargs)
        self.job_titles = job_titles or []
        self.current_date = datetime.now().strftime('%Y-%m-%d')
        self.job_data = []

    def start_requests(self):
        for job_title in self.job_titles:
            for num in range(0, 1):
                url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={job_title}&location=India&geoId=102713980&f_TPR=&f_E=2&position=1&pageNum=1&start={num*10}"
                yield Request(url, callback=self.parse_search_results, meta={'job_title': job_title})

    def parse_search_results(self, response):
        job_title = response.meta['job_title']
        soup = scrapy.Selector(response)
        divs = soup.css('div.base-card.relative.w-full.hover\\:no-underline.focus\\:no-underline.base-card--link.base-search-card.base-search-card--link.job-search-card')

        if not divs:
            return

        for d in divs:
            a_tag = d.css('a.base-card__full-link.absolute.top-0.right-0.bottom-0.left-0.p-0::attr(href)').get()
            if a_tag:
                job_link = response.urljoin(a_tag)
                yield Request(job_link, callback=self.parse_individual_job, meta={'job_title': job_title})

    def parse_individual_job(self, response):
        job_title = response.meta['job_title']
        
        # Extract company name
        company_name = response.css('a.topcard__org-name-link.topcard__flavor--black-link::text').get(default='N/A').strip()

        # Extract job description
        description_element = response.css('div.show-more-less-html__markup.show-more-less-html__markup--clamp-after-5.relative.overflow-hidden').get()
        if description_element:
            description_texts = response.css('div.show-more-less-html__markup.show-more-less-html__markup--clamp-after-5.relative.overflow-hidden *::text').getall()
            cleaned_content = "\n".join(description_texts).strip()
        else:
            cleaned_content = 'N/A'

        # Extract job title
        job_title_text = response.css('h1.top-card-layout__title.font-sans.text-lg.papabear\\:text-xl.font-bold.leading-open.text-color-text.mb-0.topcard__title::text').get(default='N/A').strip()

        self.job_data.append({
            'job_title': job_title_text,
            'company_name': company_name,
            'description': cleaned_content
        })

    def closed(self, reason):
        for job_title in self.job_titles:
            job_specific_data = [job for job in self.job_data if job['job_title'] == job_title]
            df = pd.DataFrame(job_specific_data)
            filename = f'{job_title}_{self.current_date}.csv'
            print(f'DataFrame for {job_title}:')
            print(df)
            df.to_csv(filename, index=False)
            self.log(f'Saved: {filename}')
