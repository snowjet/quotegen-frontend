import httpx
from core.log import logger
from core.config import settings
from pydantic import BaseModel
from typing import Optional

from requests.exceptions import HTTPError

class Image(BaseModel):
    image: Optional[str]
    name: Optional[str] = None
    detail: Optional[str] = None

def get_image_simple(url):

    try:
        url = settings.image_backend_api

        with httpx.Client() as client:
            
            logger.info("URL: " + url)

            response = client.get(url)
            response.raise_for_status()
        try:
            json_object = response.json()
            if 'image' in json_object:
                return {'image': json_object['image']}
            else:
                raise ValueError
        except ValueError as e:
            error_msg = "Not Valid JSON"
            logger.error(error_msg)
            return Image(name='error', Image=error_msg)

    except httpx.RequestError as exc:
        error_msg = f"An error occured while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.HTTPStatusError as exc:
        error_msg = f"Error response {exc.response.status_code} while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.HTTPError as exc:
        error_msg = f"HTTPError Error while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)

    except httpx.InvalidURL as exc:
        error_msg = f"Error while requesting {exc.request.url!r}."
        logger.error(error_msg)
        return Image(name='error', Image=error_msg)
