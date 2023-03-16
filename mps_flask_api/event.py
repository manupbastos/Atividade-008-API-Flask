from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H;%M,%S"))


EVENT = {
    "100": {
        "event_name": "Show do Loona",
        "event_id": "100",
        "event_description": "Show do meu grupo",
        "event_date": "19/04/2023",
        "timestamp": get_timestamp()
    },
    "200": {
        "event_name": "Entrevista na TV",
        "event_id": "200",
        "event_date": "13/06/2023",
        "event_description": "Entrevista com a Ellen",
        "timestamp": get_timestamp()
    },
    "300": {
        "event_name": "Aventura",
        "event_id": "300",
        "event_date": "22/08/2023",
        "event_description": "Entregar o mapa para o Diego",
        "timestamp": get_timestamp()
    }
}


def read_all():
    return list(EVENT.values())


def create(event):
    event_id = event.get("event_id")
    event_name = event.get("event_name", "")
    event_description = event.get("event_description", "")
    event_date = event.get("event_date", "")

    if event_id and event_id not in EVENT:
        EVENT[event_id] = {
            "event_id": event_id,
            "event_name": event_name,
            "event_description": event_description,
            "event_date": event_date,
            "timestamp": get_timestamp(),
        }
        return EVENT[event_id], 201
    else:
        abort(
            406,
            f"Event with last name {event_id} already exits",
        )


def read_one(event_id):
    if event_id in EVENT:
        return EVENT[event_id]
    else:
        abort(
            404, f"Person with ID {event_id} not found"
        )


def update(event_id, event):
    if event_id in EVENT:
        EVENT[event_id]["event_name"] = event.get("event_name", EVENT[event_id]["event_name"])
        EVENT[event_id]["event_date"] = event.get("event_date", EVENT[event_id]["event_date"])
        EVENT[event_id]["event_description"] = event.get("event_description", EVENT[event_id]["event_description"])
        EVENT[event_id]["timestamp"] = get_timestamp()
        return EVENT[event_id]
    else:
        abort(
            404,
            f"Person with ID {event_id} not found"
        )


def delete(event_id):
    if event_id in EVENT:
        del EVENT[event_id]
        return make_response(
            f"{event_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with ID {event_id} not found"
        )
