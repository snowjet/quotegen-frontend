import httpx
from core.log import logger

from requests.exceptions import HTTPError
from pydantic import BaseModel, ValidationError


class Quote(BaseModel):
    name: str
    quote: str


def check_message_validity(json_object):
    if "quotes" in json_object:
        try:
            logger.info("Message Contains!")
            quote = Quote.parse_obj(json_object["quotes"])
            return quote
        except ValidationError:
            logger.error("Something went wrong!")
            raise ValueError
    elif "detail" in json_object:
        raise ValueError
    else:
        raise ValueError


def get_quote_simple(url):

    try:
        with httpx.Client() as client:
            response = client.get(url)
            response.raise_for_status()
    except httpx.RequestError as exc:
        logger.error(f"An error occured while requesting {exc.request.url!r}.")
        return {
            "name": "error",
            "quote": f"An error occured while requesting {exc.request.url!r}.",
        }
    except httpx.HTTPStatusError as exc:
        logger.error(
            f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        )
        return {"name": "error", "quote": exc}
    else:
        try:
            json_object = response.json()
            return check_message_validity(json_object)
        except ValueError as e:
            logger.info("Not Valid JSON")
            return {"name": "error", "quote": "Not Valid JSON"}


async def get_quote_async(url):

    try:
        with httpx.Client() as client:
            response = client.get(url)
            response.raise_for_status()
    except httpx.RequestError as exc:
        logger.error(f"An error occured while requesting {exc.request.url!r}.")
        return {
            "name": "error",
            "quote": f"An error occured while requesting {exc.request.url!r}.",
        }
    except httpx.HTTPStatusError as exc:
        logger.error(
            f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        )
        return {"name": "error", "quote": exc}
    else:
        try:
            json_object = response.json()
            logger.info("Success!")
            return json_object
        except ValueError as e:
            logger.info("Not Valid JSON")
            return {"name": "error", "quote": "Not Valid JSON"}
