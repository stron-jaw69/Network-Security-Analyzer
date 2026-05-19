# OpenSearch client wrapper for indexing security events
from opensearchpy import OpenSearch
from typing import Dict, Any

def get_client() -> OpenSearch:
    return OpenSearch(
        hosts=[{"host": "localhost", "port": 9200}],
        http_auth=("admin", "admin"),
        use_ssl=False,
        verify_certs=False,
    )

def index_event(index: str, doc: Dict[str, Any]):
    client = get_client()
    client.index(index=index, body=doc)
