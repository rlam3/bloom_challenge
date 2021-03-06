import re
import csv


def super_man(input_file, csv_file_name, CreditTag, ConsumerTagScore, Consumer):
    """
    'test.dat' to 'test.csv'
    'test.csv' insert into postgres
    """

    # 1. Parse .dat file / Convert file
    parse_to_csv(input_file, csv_file_name)

    # 2. Create credit tags
    create_credit_tags(csv_file_name, CreditTag)

    # 3. Insert data
    insert_data(csv_file_name, Consumer, ConsumerTagScore, CreditTag)

    return None


def parse_to_csv(input_file: str, output_file: str):
    """Parse records by csv file"""

    print('parse_to_csv....')

    with open(input_file) as dat_file:
        with open(output_file, mode='w') as csv_file:

            spamwriter = csv.writer(
                csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # spamwriter.writerow(['name', 'ssn', 'tags'])

            counter = 0

            # Read Data
            for row in dat_file:
                # Parse data first 72 characters are the name
                name: str = row[:72].strip()
                # Parse data next 6 characters are the ssn
                ssn: int = row[72:81]
                # Parse tags next
                tags = row[81:]

                # loop through tags and split every 9th character
                tags = [x for x in re.findall('.........', tags)]

                # print(f'{name} : {ssn} : {tags}')
                counter += 1
                print(f'{name} : {ssn} : {counter}')

                # Write data to csv file
                spamwriter.writerow([name, ssn, *tags])


def parse_csv():
    """Parse records by csv file"""

    data = []

    with open('test2.csv') as csv_file:
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for row in spamreader:
            data.append(row)

    return data


def insert_data(c_file: str, Consumer, ConsumerTagScore, ConsumerTag):
    """Insert data into database"""
    # Consumer is passed in to give access to db and be in the right context

    # from models.consumer import Consumer

    print('insert_data....')

    with open(c_file) as csv_file:
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='"')
        # Skip header
        list_of_headers = next(spamreader)
        cleaned_tag_names = [x.strip() for x in list_of_headers[2:]]
        # Loop through data

        counter = 0

        for row in spamreader:
            name: str = row[0]
            ssn: int = row[1]
            tags = row[2:]

            counter += 1

            print(f'{name} : {ssn} : {counter}')

            # Insert data into database
            con = Consumer.create(name=name, ssn=int(ssn))

            # Loop through tags scores and insert into database
            for indx, score in enumerate(tags):
                ct_id = ConsumerTag.get_where(
                    name=cleaned_tag_names[indx])[0].id
                ConsumerTagScore.create(
                    consumer_id=con.uuid.hex,
                    credit_tag_id=ct_id,
                    score=int(score),
                )


def create_credit_tags(file_name: str, CreditTag):
    """Create credit tags"""

    print('credit_card_tags....')

    with open(file_name) as csv_file:
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='"')
        # Get header
        header = next(spamreader)
        for x in header[2:]:
            CreditTag.create(name=x.strip(), commit=True)
            print(x.strip())
