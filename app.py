from connect import client


waiting = True
db = client.test

def main(operator):
    text = operator.split(":")

    match text[0]:
        case "name":
            author_id = db.author.find({'fullname':'Albert Einstein'})[0].get('_id')
            result = db.quote.find({'author':author_id})
            return(result)
        case "tag":
            result = db.quote.find({'tags':text[1].strip()})
            return(result)
        case "tags":
            try:
                mult_tags = text[1].strip().split(",")
                result = db.quote.find({"$or": [{"tags": mult_tags[0]}, {"tags": mult_tags[1]}]})
                return(result)
            except(IndexError):
                return 'Need more than 1 tag!'
        case _:
            return "Unknown command"

if __name__ == "__main__":
    while waiting == True:
        operator = input(":")
        endValue = operator.find("exit")
        if endValue != -1:
            break
        else: 
            if not isinstance(main(operator), str):
                for i in main(operator):
                    print(i)
            else:
                print(main(operator))