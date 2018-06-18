from elasticsearch import Elasticsearch
import hashlib
es = Elasticsearch(hosts=["127.0.0.1"])
import redis
r = redis.Redis(host='127.0.0.1',port=6379)

all_urls = es.search(
                index="jobbole",
                request_timeout=60,
                size = 5000,
                body={
                "query":{
                    "match_all" : {
                            }
                    }
                    }

            )
with open('urls.txt','w')as f:
    for urla in all_urls['hits']['hits']:
        url = urla['_source']['url']
        # dupefilter sha1值
        # url_rpf = hashlib.sha1(url.encode('utf-8')).hexdigest()
        r.lpush('redis_jobbole:requests',url)