from datetime import datetime, timedelta
from newsapi import NewsApiClient
from api_key import API_KEY

# busca = input('Insira a pesquisa: ')
searching = "Microsoft"

newsapi = NewsApiClient(api_key = API_KEY)

sources = newsapi.get_sources(
    country= "br"
)


sources_ids = [source['id'] for source in sources['sources']]
domains_url = [domain['url'] for domain in sources['sources']]

sources_ids_str = ','.join(sources_ids)
domains_url_str = ','.join(domains_url)

date_today = datetime.now()
final_date = date_today - timedelta(days=29)

content = newsapi.get_everything(
    q= searching,
    sources= sources_ids_str,
    domains= domains_url_str,
    from_param= final_date,
    to= date_today,
    language='pt',
    sort_by='publishedAt'
)

for article in content['articles']:
    source_name = article['source']['name']
    title = article['title'][:50]  
    url = article['url']
    print(f"Fonte: {source_name} - Título: {title}... - URL: {url}")
