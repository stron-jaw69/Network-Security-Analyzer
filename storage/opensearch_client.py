#index events in the network security pipeline
from opensearchpy import OpenSearch
from config import OPENSEARCH_HOST, OPENSEARCH_PORT

client = OpenSearch(
    hosts=[{"host": OPENSEARCH_HOST, "port": OPENSEARCH_PORT}],
    use_ssl=False
)

def index_event(index, doc):
    client.index(index=index, body=doc)
