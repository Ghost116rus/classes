
class Event:

    def __init__(self, input_data):
        input_data = input_data.split('*')
        self.description = input_data[0]
        self._date = self._set_date(input_data[1])

    def _set_date(self, value):
        temp = []
        if len(value) == 3:
            temp[0] = value[0]
            temp[1] = value[1]
            temp[2] = value[2]
        else:
            temp = ["2023", "02", "04"]

        return temp

    date = property()

    @date.getter
    def date(self):
        return f"Day:{self._date[0]} Month:{self._date[1]} Year:{self._date[2]}"


def main():
    new_event = Event("Встреча с друзьями * 12-11-2001")
    print(f"Description {new_event.description}")
    check = new_event.date
    print(f"{new_event.date}")


main()
