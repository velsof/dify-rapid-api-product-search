import os
import json
import requests
from typing import Dict, List, Optional, Any

class RapidAPIProductSearch:
    def __init__(self, settings: Dict[str, Any]):
        """Initialize the RapidAPI Product Search class."""
        self.api_key = settings.get("rapid_api_key", "")
        self.base_url = settings.get("base_url", "https://real-time-product-search.p.rapidapi.com")
        if not self.api_key:
            raise ValueError("RapidAPI Key is required")

        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.base_url.replace("https://", "")
        }

    def search_products(self, query: str, **kwargs) -> Dict[str, Any]:
        """
        Search for products across multiple stores.
        
        Args:
            query: The search query
            **kwargs: Optional parameters like limit, page, country, etc.
        
        Returns:
            Dict containing search results
        """
        endpoint = f"{self.base_url}/search"
        params = {
            "query": query,
            **kwargs
        }
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_product_details(self, product_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific product.
        
        Args:
            product_id: The ID of the product
        
        Returns:
            Dict containing product details
        """
        endpoint = f"{self.base_url}/product/{product_id}"
        
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_product_offers(self, product_id: str, **kwargs) -> Dict[str, Any]:
        """
        Get offers for a specific product.
        
        Args:
            product_id: The ID of the product
            **kwargs: Optional parameters like limit, page, etc.
        
        Returns:
            Dict containing product offers
        """
        endpoint = f"{self.base_url}/offers/{product_id}"
        params = {**kwargs}
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_product_reviews(self, product_id: str, **kwargs) -> Dict[str, Any]:
        """
        Get reviews for a specific product.
        
        Args:
            product_id: The ID of the product
            **kwargs: Optional parameters like limit, page, sort, etc.
        
        Returns:
            Dict containing product reviews
        """
        endpoint = f"{self.base_url}/reviews/{product_id}"
        params = {**kwargs}
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_deals(self, **kwargs) -> Dict[str, Any]:
        """
        Get current deals and promotions.
        
        Args:
            **kwargs: Optional parameters like category, store, limit, etc.
        
        Returns:
            Dict containing deals
        """
        endpoint = f"{self.base_url}/deals"
        params = {**kwargs}
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_store_reviews(self, store_id: str, **kwargs) -> Dict[str, Any]:
        """
        Get reviews for a specific store.
        
        Args:
            store_id: The ID of the store
            **kwargs: Optional parameters like limit, page, sort, etc.
        
        Returns:
            Dict containing store reviews
        """
        endpoint = f"{self.base_url}/store-reviews/{store_id}"
        params = {**kwargs}
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
