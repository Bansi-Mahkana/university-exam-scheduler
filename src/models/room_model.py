class Room:
    def __init__(self, room_id, capacity, availability=None):
        self.room_id = room_id
        self.capacity = capacity

        if availability is None:
            self.availability = []
        else:
            self.availability = availability