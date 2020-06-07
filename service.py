import json
import logging
from operator import itemgetter

import boto3
import requests
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup

url = "https://v3.petstablished.com/organization/14/widget/dogs"
base_selector = "#wrapper div.pet-container > a.pet-link > div.pet-description"

s3 = boto3.client("s3")


def handler(event, context):
    puppies = scrape()
    try:
        s3.put_object(
            Bucket="puppies-ddh",
            Body=json.dumps(puppies),
            Key="puppies.json",
            ContentType="application/json",
        )
        print(f" 🐶 Found {len(puppies)} puppies")
    except ClientError as e:
        logging.error(e)
        return False
    return True


def scrape():
    page = requests.get(url)
    puppies = []
    content = BeautifulSoup(page.content, 'html.parser')
    for pup in content.select(base_selector):
        name = pup.select("h3.nomargin")[0].get_text().strip()
        age = pup.select("i")[0].get_text().strip().split()[1]
        breed = pup.select("i")[0].get_text().strip()
        pup = {
            "name": name,
            "age": age,
            "breed": breed
        }
        puppies.append(pup)

    sorted_puppies = sorted(puppies, key=itemgetter('age'))
    # print(f" 🐶 Found {len(sorted_puppies)} puppies")
    # with open('puppies.json', 'w') as f:
    #     json.dump(sorted_puppies, f)
    return sorted_puppies

# print(scrape())
# scrape()
