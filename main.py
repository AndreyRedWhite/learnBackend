from fastapi import FastAPI, Query, Body
import uvicorn

app = FastAPI()

hotels = [
    {"id": 1, "title": "sochi", "name": "Sochi_Star"},
    {"id": 2, "title": "dubai", "name": "Dubai_parus"}
]


@app.get("/")
def root():
    return "hello word"


@app.get("/hotels")
def get_hotels(
    id: int | None = Query(default=None, description='ID отеля'),
    title: str | None = Query(default=None, description='Название отеля')
):
    hotels_ = []
    for hotel in hotels:
        if id and hotel['id'] != id:
            continue
        if title and hotel['title'] != title:
            continue
        hotels_.append(hotel)
    return hotels_
    # return [hotel for hotel in hotels if hotel['title'] == title and hotel['id'] == id]


@app.delete('/hotels/{hotel_id}')
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {'status': 'OK'}


@app.post("/hotels")
def add_hotel(
    title: str = Body(embed=True),
    name: str = Body(embed=True)
    ):
    global hotels
    hotels.append({
        "id": hotels[-1]['id'] + 1,
        "title": title,
        'name': name
    })
    return {'status': 'OK'}


@app.put("/hotels/{hotel_id}")
def update_hotel(
    hot_id: int = Body(embed=True),
    title: str = Body(embed=True),
    name: str = Body(embed=True)
    ):
    global hotels
    for hotel in hotels:
        if hotel['id'] == hot_id:
            hotel['title'] = title
            hotel['name'] = name
            return {"status": "OK"}
        else:
            return {'status': 'bad parameter'}


@app.patch("/hotels/{hotel_id}")
def patch_hotel(
    hot_id: int = Body(embed=True),
    title: str | None = Body(default=None, embed=True, strict=False),
    name: str | None = Body(default=None, embed=True, strict=False)
    ):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hot_id:
            if title:
                hotel['title'] = title
            if name:
                hotel['name'] = name
            return {"status": "OK"}
        else:
            return {'status': 'bad parameter'}


def main():
    uvicorn.run("main:app", reload=True)


if __name__ == '__main__':
    main()