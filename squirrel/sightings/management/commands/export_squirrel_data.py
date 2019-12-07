import csv
from django.core.management import BaseCommand
from sightings.models import squirrel
class Command(BaseCommand):
    help = 'export a csv file from  the database'
    def add_arguments(self,parser):
        parser.add_argument('csv_file')
        #parser.add_argument('', type=str)
    
    def handle(self, *args, **options): 
        with open(options['csv_file'],'w') as f:
            names = ['Y','X','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from']
            writer = csv.DictWriter(f,fieldnames=names)
            squirrels = squirrel.objects.all()
            for item in squirrels:
                writer.writerow({'Y': item.latitude})
                writer.writerow({'X': item.longitude})
                writer.writerow({'Unique Squirrel ID': item.uniqueid})
                writer.writerow({'Shift': item.shift})
                writer.writerow({'Date': item.Date})
                writer.writerow({'Age': item.Age})
                writer.writerow({'Primary Fur Color': item.furcolor})
                writer.writerow({'Location': item.location})
                writer.writerow({'Specific Location': item.specificlocation})
                writer.writerow({'Running': item.running})
                writer.writerow({'Chasing': item.chasing})
                writer.writerow({'Climbing': item.climbing})
                writer.writerow({'Eating': item.eating})
                writer.writerow({'Foraging': item.foraging})
                writer.writerow({'Other Activities': item.otheractivities})
                writer.writerow({'Kuks': item.kuks})
                writer.writerow({'Quaas': item.quaas})
                writer.writerow({'Moans': item.moans})
                writer.writerow({'Tail flags': item.tailflags})
                writer.writerow({'Tail twitches': item.tailtwitches})
                writer.writerow({'Approaches': item.approaches})
                writer.writerow({'Indifferent': item.indifferent})
                writer.writerow({'Runs from': item.runsfrom})
            f.close()
                


