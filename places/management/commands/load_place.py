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
        except requests.exceptions.HTTPError as e:
            logger.error(f'UNABLE TO LOAD DATA FROM RESOURCE {resource_url}, details: {e}')
            return

        place_data = response.json()
        place, created = Place.objects.get_or_create(
            title=place_data['title'],
            defaults={
                'short_title': place_data['title'],
                'short_description': place_data['description_short'],
                'long_description': place_data['description_long'],
                'lng': place_data['coordinates']['lng'],
                'lat': place_data['coordinates']['lat'],
                'place_id': place_data['title'],
            }
        )
        if created:
            for i, img_url in enumerate(place_data['imgs'], start=1):
                try:
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    logger.error(f'UNABLE TO SAVE IMAGE FROM FROM RESOURCE {img_url}, details: {e}')
                    continue

                img = BytesIO(img_response.content)
                place_image, img_created = PlaceImage.objects.get_or_create(
                    place=place,
                    position=i
                )
                place_image.image.save(f'place-{place.id}-img-{i}', img, save=True)

        action = 'CREATED' if created else 'UPDATED'
        logger.info(f'{action} PLACE {place}')

        logger.info(f'END LOADING DATA FROM RESOURCE {resource_url}')
