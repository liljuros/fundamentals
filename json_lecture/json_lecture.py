import json
json_str = '''
{
    "name": "Eric Smith",
    "age": 32,
    "phonenumbers": [
        {
            "type": "home",
            "number": "(212) 555-3276"
        },
        {
            "type": "work",
            "number": "(332) 555-1234"
        }
        ],
    "spouse": null,
    "children": [],
    "employed": true
}
'''

erik = json.loads(json_str)
print(erik)
print(json.dumps(erik, indent=2))