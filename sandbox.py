from pydantic import BaseModel
test_user = {"id" : 2}
z = [{"title": "first title", "content": "first content", "owner_id": test_user['id']},
     {"title": "first title", "content": "first content", "owner_id": 4}, ]
class B(BaseModel):
    title:str
    content:str
    owner_id: int
a = B(**z)
print(a.title)