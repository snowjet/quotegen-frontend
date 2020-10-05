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
            
            logger.info("URL: " + url)

            response = client.get(url)
            response.raise_for_status()
        try:
            json_object = response.json()
            return check_message_validity(json_object)
        except ValueError as e:
            error_msg = "Not Valid JSON"
            logger.error(error_msg)
            return Quote(name='error', quote=error_msg)

    except httpx.RequestError as exc:
        error_msg = f"An error occured while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Quote(name='error', quote=error_msg)

    except httpx.HTTPStatusError as exc:
        error_msg = f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Quote(name='error', quote=error_msg)

    except httpx.HTTPError as exc:
        error_msg = f"HTTPError Error while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Quote(name='error', quote=error_msg)

    except httpx.InvalidURL as exc:
        error_msg = f"Error while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Quote(name='error', quote=error_msg)
