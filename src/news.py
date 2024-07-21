from datetime import datetime, timedelta
from newsapi import NewsApiClient
from api_key import API_KEY

# busca = input('Insira a pesquisa: ')
busca = "incêndio florestal"

newsapi = NewsApiClient(api_key = API_KEY)

sources = newsapi.get_sources(
    country= "br"
)


sources_ids = [source['id'] for source in sources['sources']]
domains_url = [source['url'] for source in sources['sources']]

sources_ids_str = ','.join(sources_ids)
domains_url_str = ','.join(domains_url)

data_hoje = datetime.now()
data_final = data_hoje - timedelta(days=29)

all = newsapi.get_everything(
    q= busca,
    sources= sources_ids_str,
    domains= domains_url_str,
    from_param= data_final,
    to= data_hoje,
    language='pt',
    sort_by='publishedAt'
)

for article in all['articles']:
    source_name = article['source']['name']
    title = article['title'][:50]  
    url = article['url']
    print(f"Fonte: {source_name} - Título: {title}... - URL: {url}")
