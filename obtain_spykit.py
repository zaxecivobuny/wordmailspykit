import datetime
from mtgsdk import Card


def main():
    print("obtaining cards")
    # cards = Card.where(type="creature").where(set="v09").all()
    # cards = Card.where(type="creature").where(set="v09,v17").all()

    cards = Card.where(type="creature").all()
    print(len(cards), "cards obtained")
    print(datetime.datetime.now())

    card_name_set = set()
    for i in cards:
        # print(i.name)
        card_name_set.add(i.name)

    # print(card_name_set)

    word_count = 0
    for i in card_name_set:
        # print(word_count, i)
        word_count += 1
        word_count += i.count(' ')
        # print(word_count)

    print("word count is:", word_count)

if __name__ == '__main__':
    print(datetime.datetime.now())
    main()
    print(datetime.datetime.now())
