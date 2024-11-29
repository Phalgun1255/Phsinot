# utils/feature_extraction.py

import re
from urllib.parse import urlparse

class FeatureExtraction:
    def __init__(self, url):
        self.url = url

    def getFeaturesList(self):
        features = []
        
        # Feature 1: URL Length
        features.append(len(self.url))
        
        # Feature 2: Number of dots (.)
        features.append(self.url.count('.'))
        
        # Feature 3: Number of hyphens (-)
        features.append(self.url.count('-'))
        
        # Feature 4: Number of question marks (?)
        features.append(self.url.count('?'))
        
        # Feature 5: Number of '@' symbols
        features.append(self.url.count('@'))
        
        # Feature 6: Check if 'https' is present (secure connection)
        features.append(1 if 'https' in self.url else 0)
        
        # Feature 7: URL contains www
        features.append(1 if 'www' in self.url else 0)
        
        # Feature 8: Number of slashes (/)
        features.append(self.url.count('/'))
        
        # Feature 9: Presence of suspicious domain (e.g., ".xyz")
        features.append(1 if any(x in self.url for x in ['.xyz', '.club', '.top']) else 0)
        
        # Feature 10: Length of the domain name
        domain = urlparse(self.url).hostname
        if domain:
            features.append(len(domain))
        else:
            features.append(0)
        
        # You can add more features based on your project needs
        
        return features
