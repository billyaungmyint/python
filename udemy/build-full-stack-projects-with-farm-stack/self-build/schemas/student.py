# schema helps to serialize and convert mongodb format json to our UI need

def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone": db_item["student_phone"],
    }
    
def listOfStudentEntity(db_item_list) -> list:
    #return [StudentEntity(item) for item in db_item_list]
    list_stud_entity = []
    for item in db_item_list:
        list_stud_entity.append(studentEntity(item))
        
    return list_stud_entity



