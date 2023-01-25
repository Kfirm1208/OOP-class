record_collection = {
  2548: {
    'albumTitle': 'Slippery When Wet',
    'artist': 'Bon Jovi',
    'tracks': ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    'albumTitle': '1999',
    'artist': 'Prince',
    'tracks': ['1999', 'Little Red Corvette']
  },
  1245: {
    'artist': 'Robert Palmer',
    'tracks': []
  },
  5439: {
    'albumTitle': 'ABBA Gold'
  }
}


def update_records(record, id, property, value):
  #check id in dict donlt have id return record
  if id in record.keys():
    # change data
    if property != "tracks" and value != "":
      # add property
      record[id].update({property: value})

    elif property == 'tracks' and 'tracks' not in record[id].keys():
      record[id].append({'tracks': []})
      #add value in list
      record[id][property].append(value)
      
    # have value input
    elif property == 'tracks' and value != '':
      record[id][property].append(value)
    # don't have value
    elif value == "":
      #delete the value
      del record[id][property]

    return record

  return record
