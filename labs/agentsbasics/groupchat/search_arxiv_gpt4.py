# filename: search_arxiv_gpt4.py
import requests
from bs4 import BeautifulSoup

def search_arxiv(query, max_results=1):
    url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'xml')
        entries = soup.find_all('entry')
        papers = []
        for entry in entries:
            paper = {
                'title': entry.title.text,
                'summary': entry.summary.text,
                'published': entry.published.text,
                'link': entry.id.text
            }
            papers.append(paper)
        return papers
    else:
        print("Error fetching data from arXiv")
        return []

# Search for the latest paper about GPT-4
papers = search_arxiv('GPT-4', max_results=1)
for paper in papers:
    print(f"Title: {paper['title']}")
    print(f"Published: {paper['published']}")
    print(f"Summary: {paper['summary']}")
    print(f"Link: {paper['link']}")