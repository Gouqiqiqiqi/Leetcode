import aiohttp
import asyncio

# fetch JSON items from a URL
async def fetch_data(session, url):
    resp = session.get(url)
    data = await resp.json
    return data.get("items", [])

# process multiple URLs and filter by threshold
async def process_urls(urls, threshold):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    filtered = [item for batch in results for item in batch if item["value"] > threshold]
    return filtered

if __name__ == "__main__":
    urls = ["https://api.example.com/data1", "https://api.example.com/data2"]
    data = asyncio.run(process_urls(urls, 10))
    print("Filtered items:", data)