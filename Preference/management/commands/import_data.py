import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from Preference.models import DataEntry
from datetime import datetime

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def handle(self, *args, **options):
        json_file_path = os.path.join(settings.BASE_DIR, 'jsondata.json')

        try:
            with open(json_file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

                for item in data:
                    # Handle the intensity field
                    try:
                        intensity = float(item.get('intensity', 0))
                    except (ValueError, TypeError):
                        self.stdout.write(self.style.WARNING(f"Invalid intensity value: {item.get('intensity')}"))
                        intensity = 0  # Set to a default value

                    # Handle empty or missing added field
                    added_str = item.get('added', '')
                    if added_str:
                        try:
                            added = datetime.strptime(added_str, "%B, %d %Y %H:%M:%S")
                        except ValueError:
                            self.stdout.write(self.style.WARNING(f"Invalid date/time format: {added_str}"))
                            added = None
                    else:
                        added = None

                    # Handle empty or missing published field
                    published_str = item.get('published', '')
                    if published_str:
                        try:
                            published = datetime.strptime(published_str, "%B, %d %Y %H:%M:%S")
                        except ValueError:
                            self.stdout.write(self.style.WARNING(f"Invalid date/time format: {published_str}"))
                            published = None
                    else:
                        published = None

                    # Handle the likelihood field
                    likelihood = item.get('likelihood', None)
                    if likelihood == '':
                        likelihood = None
                    else:
                        try:
                            likelihood = int(likelihood)
                        except (ValueError, TypeError):
                            self.stdout.write(self.style.WARNING(f"Invalid likelihood value: {likelihood}"))
                            likelihood = None

                    DataEntry.objects.create(
                        end_year=item['end_year'],
                        intensity=intensity,
                        sector=item['sector'],
                        topic=item['topic'],
                        insight=item['insight'],
                        url=item['url'],
                        region=item['region'],
                        start_year=item['start_year'],
                        impact=item['impact'],
                        added=added,
                        published=published,
                        country=item['country'],
                        relevance=item['relevance'],
                        pestle=item['pestle'],
                        source=item['source'],
                        title=item['title'],
                        likelihood=likelihood,
                    )

                self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {json_file_path}'))
