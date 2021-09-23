import logging
import requests

from io import BytesIO
from django.core.management import BaseCommand

from places.models import Place, PlaceImage

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Load information about places with media files'

    def add_arguments(self, parser):
        parser.add_argument('resource_url', type=str)

    def handle(self, *args, **options):
        resource_url = options['resource_url']

        logger.info(f'START LOADING DATA FROM RESOURCE {resource_url}')

        try:
            response = requests.get(resource_url)
            response.raise_for_status()
            place_data = response.json()
            place, created = Place.objects.get_or_create(
                title=place_data['title'],
                title_short=place_data['title'],
                description_short=place_data['description_short'],
                description_long=place_data['description_long'],
                lng=place_data['coordinates']['lng'],
                lat=place_data['coordinates']['lat'],
                place_id=place_data['title'],
            )
            for i, img_url in enumerate(place_data['imgs']):
                try:
                    index = i + 1
                    img_response = requests.get(img_url)
                    img = BytesIO(img_response.content)
                    place_image, img_created = PlaceImage.objects.get_or_create(
                        place=place,
                        position=index
                    )
                    place_image.image.save(f'place-{place.id}-img-{index}', img, save=True)
                except Exception as e:
                    logger.error(f'UNABLE TO SAVE IMAGE FROM FROM RESOURCE {img_url}, details: {e}')

            action = 'CREATED' if created else 'UPDATED'
            logger.info(f'{action} PLACE {place}')

        except Exception as e:
            logger.error(f'UNABLE TO LOAD DATA FROM RESOURCE {resource_url}, details: {e}')

        logger.info(f'END LOADING DATA FROM RESOURCE {resource_url}')
