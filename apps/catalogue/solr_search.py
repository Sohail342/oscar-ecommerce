from haystack.backends.solr_backend import SolrSearchBackend

class CustomSolrSearchBackend(SolrSearchBackend):
    def _process_results(self, raw_results, **kwargs):
        results = super()._process_results(raw_results, **kwargs)
        for result in results['results']:
            if isinstance(result.django_ct, list) and result.django_ct:
                result.django_ct = result.django_ct[0]
        return results