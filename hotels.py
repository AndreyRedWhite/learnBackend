from fastapi import Query, Body, APIRouter

from schemas.hotels_schema import HotelData

router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get(path="", summary='Get all the hotels')
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


@router.delete(path='/{hotel_id}', summary='Delete an particular hotel')
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {'status': 'OK'}


@router.post(path="", summary='Add new wonderful hotel')
def add_hotel(data: HotelData):
    global hotels
    hotels.append({
        "id": hotels[-1]['id'] + 1,
        "title": data.title,
        'name': data.name
    })
    return {'status': 'OK'}


@router.put(path="/{hotel_id}", summary='Update all the info about particular hotel')
def update_hotel(
    hotel_id: int, data: HotelData):
    global hotels
    for hotel in hotels:
        if hotel['id'] == hotel_id:
            hotel['title'] = data.title
            hotel['name'] = data.name
            return {"status": "OK"}
        else:
            return {'status': 'bad parameter'}


@router.patch(path="/{hotel_id}", summary='Partially update an info about particular hotel')
def patch_hotel(
    hotel_id: int,
    title: str | None = Body(default=None, embed=True, strict=False),
    name: str | None = Body(default=None, embed=True, strict=False)
    ):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if title:
                hotel['title'] = title
            if name:
                hotel['name'] = name
            return {"status": "OK"}
        else:
            return {'status': 'bad parameter'}
